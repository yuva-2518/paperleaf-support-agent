"""
Setup check.

Run it from the project folder:
    Mac:      .venv/bin/python check_setup.py
    Windows:  .venv\\Scripts\\python check_setup.py

It prints OK, or a FIX line telling you what to do, for each thing the project needs.
It never prints your key.
"""

import importlib.metadata
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_FOLDER = Path(__file__).resolve().parent
ENV_FILE = PROJECT_FOLDER / ".env"
PLACEHOLDER_KEY = "paste-your-key-here"

# Python versions this project supports. We tested on 3.13.
SUPPORTED_PYTHON = [(3, 11), (3, 12), (3, 13)]

# The packages from requirements.txt that the project imports.
PACKAGES = ["google-adk", "python-dotenv", "chromadb", "streamlit"]

problems = 0


def ok(message):
    print(f"  OK    {message}")


def fix(message, how):
    global problems
    problems += 1
    print(f"  FIX   {message}")
    print(f"        -> {how}")


def check_python():
    version = sys.version_info[:2]
    shown = f"{version[0]}.{version[1]}"
    if version in SUPPORTED_PYTHON:
        ok(f"Python {sys.version.split()[0]}")
    else:
        fix(
            f"Python {shown} is not supported here (use 3.11, 3.12 or 3.13; we tested 3.13).",
            "Install Python 3.13 from python.org, then ask Claude Code to rebuild the .venv folder with it.",
        )


def check_virtual_environment():
    inside_venv = sys.prefix != sys.base_prefix
    if inside_venv:
        ok("Running inside the project's virtual environment (.venv)")
    else:
        fix(
            "This check is not running inside the project's .venv.",
            "Run it as  .venv/bin/python check_setup.py  (Mac)  or  .venv\\Scripts\\python check_setup.py  (Windows).",
        )


def check_packages():
    missing = []
    found = []
    for name in PACKAGES:
        try:
            found.append(f"{name} {importlib.metadata.version(name)}")
        except importlib.metadata.PackageNotFoundError:
            missing.append(name)
    if missing:
        fix(
            "Missing packages: " + ", ".join(missing),
            "Ask Claude Code: install the packages in requirements.txt into the .venv folder.",
        )
        return False
    ok("Packages installed: " + ", ".join(found))
    return True


def read_settings():
    """Reads .env and returns the settings, or None if something is wrong."""
    if not ENV_FILE.exists():
        fix(
            "There is no .env file in the project folder.",
            "Make a copy of .env.example, name it .env, and paste your Gemini key into it (session0.md, Step 4).",
        )
        return None
    ok(".env file found")

    from dotenv import dotenv_values

    settings = dotenv_values(ENV_FILE)
    key = (settings.get("GOOGLE_API_KEY") or "").strip()
    model = (settings.get("GEMINI_MODEL") or "").strip()

    if not key or key == PLACEHOLDER_KEY:
        fix(
            "The Gemini key in .env is still empty.",
            "Open .env in VS Code and replace paste-your-key-here with your key from Google AI Studio. Save the file.",
        )
        return None
    if " " in key or key.startswith(("'", '"')):
        fix(
            "The Gemini key in .env has spaces or quote marks around it.",
            "In .env the line should look like  GOOGLE_API_KEY=AIza...  with no spaces and no quotes.",
        )
        return None
    ok("Gemini key is filled in (not shown)")

    if not model:
        fix(
            "GEMINI_MODEL is missing from .env.",
            "Copy the GEMINI_MODEL line from .env.example into .env.",
        )
        return None
    ok(f"Model name set: {model}")
    return key, model


def check_gemini(key, model):
    """Sends one tiny request to Gemini to check the key and the model."""
    try:
        from google import genai

        client = genai.Client(api_key=key)
        reply = client.models.generate_content(model=model, contents="Reply with the single word OK.")
        text = (reply.text or "").strip()
        ok(f"Gemini replied using {model} ({text[:20]!r})")
    except Exception as error:  # we explain the common errors in plain words
        message = str(error)
        if "API_KEY_INVALID" in message or "API key not valid" in message:
            fix(
                "Google says the key is not valid.",
                "Copy the key again from Google AI Studio and paste it into .env (no spaces, no quotes).",
            )
        elif "404" in message or "NOT_FOUND" in message:
            fix(
                f"The model {model} was not found.",
                "Check the GEMINI_MODEL line in .env matches .env.example exactly.",
            )
        elif "429" in message or "RESOURCE_EXHAUSTED" in message:
            fix(
                "The key works, but its free limit is used up for now.",
                "Wait a minute and try again. If it says 'per day', wait until tomorrow or use a key from another Google account.",
            )
        elif "PERMISSION_DENIED" in message or "403" in message:
            fix(
                "Google refused the request (permission denied).",
                "Make a new key in Google AI Studio and paste it into .env.",
            )
        else:
            fix(
                "Could not reach Gemini: " + message[:200],
                "Check your internet connection, then run this check again.",
            )


def run_tool(command):
    """Runs a small command and returns (worked, first line of output)."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
    except Exception:
        return False, ""
    output = (result.stdout or result.stderr).strip().splitlines()
    return result.returncode == 0, (output[0] if output else "")


def check_git():
    if shutil.which("git") is None:
        fix("Git is not installed.", "Install Git from git-scm.com (session0.md, Step 1).")
        return
    worked, line = run_tool(["git", "--version"])
    ok(line if worked else "Git installed")


def check_github_cli():
    if shutil.which("gh") is None:
        fix(
            "The GitHub CLI (gh) is not installed. You need it in Session 4.",
            "Install it from cli.github.com (session0.md, Step 1).",
        )
        return
    worked, line = run_tool(["gh", "--version"])
    ok(line if worked else "GitHub CLI installed")
    logged_in, _ = run_tool(["gh", "auth", "status"])
    if logged_in:
        ok("GitHub CLI is logged in")
    else:
        fix(
            "The GitHub CLI is not logged in. You need it in Session 4.",
            "Run  gh auth login  in the terminal and follow the steps (session0.md, Step 6).",
        )


def main():
    print()
    print("Setup check")
    print("-----------")
    check_python()
    check_virtual_environment()
    if check_packages():
        settings = read_settings()
        if settings:
            check_gemini(*settings)
    check_git()
    check_github_cli()
    print()
    if problems == 0:
        print("All OK. You are ready.")
    else:
        print(f"{problems} thing(s) to fix. Fix the FIX lines above, then run this check again.")
    print()
    sys.exit(0 if problems == 0 else 1)


if __name__ == "__main__":
    main()
