# Session 0: Set up your laptop

**What you will do:** install the tools, download the starter kit, connect it to Gemini, and see a simple agent reply to "Hi". You will build that agent into a customer-support agent in the next sessions.

**About how long:** 45 to 60 minutes. Most of it is waiting for downloads, so do this before Day 1 on a good internet connection if you can.

**What you need before starting:**

- A laptop (Mac or Windows) where you can install apps.
- A Claude Pro account (for Claude Code).
- A Google account (for the free Gemini key).
- A GitHub account. Make a free one at [github.com/signup](https://github.com/signup) if you don't have one.

**Done when:** the setup check shows **All OK**, and the starter agent replies to "Hi".

**Gemini requests this guide uses:** about 2 (one in the setup check, one when you say "Hi").

---

## How these guides work

Every step looks the same:

- **Why:** what the step is for.
- **Do this** or **Paste this into Claude Code:** exactly what to do. Copy prompts word for word.
- **You should see:** what happens.
- **Check it:** a quick test, with the result you should get.
- **If it went wrong:** problems we hit when we tried it ourselves, and the fix.
- **Explain it back:** a prompt that asks Claude Code to explain the step in plain English. Do it: this is where you learn.
- **Your brief:** how this step applies to your own business.

Some rules for every session:

- **You never write code yourself.** Claude Code writes it. You ask, read, test and check.
- **Type `/clear` in Claude Code before each new step.** It gives Claude Code a fresh start, so old steps don't confuse it.
- **When Claude Code asks permission** to run a command or change a file, read what it wants to do in one line, then choose **Yes**. If something looks wrong (for example, deleting files you didn't mention), choose **No** and ask it why.
- **Never paste your Gemini key into Claude Code.** It goes in one file only, `.env`, which you edit yourself.
- Commands are shown for Mac and for Windows. Lines marked *(Windows, not tested by us)* have not been tried on a Windows laptop yet. If one fails, tell a TA.

---

## Step 1: Install the tools

**Why:** these are the five tools you use in every session.

**Do this:** install anything you don't already have.

1. **VS Code** (the editor): download it from [code.visualstudio.com](https://code.visualstudio.com) and install it.
2. **Python 3.13**: go to [python.org/downloads](https://www.python.org/downloads/) and scroll to **"Looking for a specific release?"**. Click the newest **Python 3.13.x**, then download the installer for your system (Mac: "macOS 64-bit universal2 installer"; Windows: "Windows installer (64-bit)").
   - Use **3.13**, not the bigger number on the big yellow button. Some packages this course needs don't work with Python 3.14 or 3.15 yet.
   - **Windows:** on the first installer screen, tick **"Add python.exe to PATH"** before clicking Install.
3. **Git**:
   - Mac: you install it in the check below. The first time you type `git --version`, your Mac offers to install "command line developer tools". Click **Install** and wait.
   - Windows: download it from [git-scm.com](https://git-scm.com/downloads) and install it with all the default options. *(Windows, not tested by us)*
4. **GitHub CLI** (lets Claude Code put your code on GitHub in Session 4): download it from [cli.github.com](https://cli.github.com) and install it.
5. **Claude Code**: open the Terminal app (Mac) or PowerShell (Windows) and paste the line for your system:
   - Mac:
     ```
     curl -fsSL https://claude.ai/install.sh | bash
     ```
   - Windows *(Windows, not tested by us)*:
     ```
     irm https://claude.ai/install.ps1 | iex
     ```

**Check it:** close the terminal and open a new one, so it sees the new tools. Paste these lines one at a time and press Enter after each.

- Mac:
  ```
  python3.13 --version
  git --version
  gh --version
  claude --version
  ```
- Windows *(Windows, not tested by us)*:
  ```
  py -3.13 --version
  git --version
  gh --version
  claude --version
  ```

Each line should print a version number. Python should say `Python 3.13.` followed by a number.

**If it went wrong:**

- *"command not found"* (Mac) or *"is not recognized"* (Windows): the tool isn't installed, or the terminal was opened before you installed it. Close the terminal, open a new one, and try again. If it still fails, install that tool again.
- *Python says 3.14 or 3.15:* you installed the newest Python, not 3.13. Install 3.13 as well (it can live next to the other one). The command above asks for 3.13 by name, so it will find the right one.
- *Claude Code says it needs Git for Windows:* install Git first (item 3), then open a new terminal. *(Windows, not tested by us)*

**Explain it back:** nothing to explain yet. Claude Code is not running.

**Your brief:** the same for everyone.

---

## Step 2: Download the starter kit and open it in VS Code

**Why:** the starter kit is the project you build on. It has a simple agent, the rules Claude Code follows, and a setup check.

**Do this:**

1. Download the starter kit ZIP: [github.com/abduljabbarpeer/customer-support-agent/archive/refs/heads/main.zip](https://github.com/abduljabbarpeer/customer-support-agent/archive/refs/heads/main.zip)
2. Unzip it (double-click it on Mac; on Windows, right-click it and choose **Extract All**).
3. Move the unzipped folder `customer-support-agent-main` somewhere easy to find, such as your Documents folder. You can rename it, for example to your business's name. Don't use spaces in the name.
4. Open VS Code. Choose **File > Open Folder...** and pick that folder.
5. If VS Code asks **"Do you trust the authors of the files in this folder?"**, click **Yes, I trust the authors**.

**You should see:** on the left, the files of the project: `support_agent`, `demo-data`, `CLAUDE.md`, `check_setup.py`, `session0.md` and a few more.

**Check it:** in VS Code's left panel, you can see a file called `.env.example`.

**If it went wrong:**

- *You see one folder inside another* (for example `customer-support-agent-main` inside `customer-support-agent-main`): open the inner one, the one that contains `CLAUDE.md`.

**Explain it back:** next step.

**Your brief:** the same for everyone. In Session 1 you turn this agent into your business's agent.

---

## Step 3: Start Claude Code and take a tour

**Why:** Claude Code is your builder. You type requests in plain English; it reads and changes the project for you.

**Do this:**

1. In VS Code, open the terminal: menu **Terminal > New Terminal**. A panel opens at the bottom. This is where you talk to Claude Code.
2. Type `claude` and press Enter.
3. The first time, Claude Code asks you to log in. Choose your Claude account, and a browser window opens. Log in there, then come back to VS Code.
4. If Claude Code asks whether you trust this folder, choose **Yes**.
5. Type `/model` and press Enter. Choose **Sonnet**. (This is the model we tested the guides with.)

**Paste this into Claude Code:**
> Give me a short tour of this project in plain English. What is each file and folder for? Keep it under 15 lines and don't change anything.

**You should see:** Claude Code reads the files and lists them: the agent in `support_agent/agent.py`, the settings template `.env.example`, the setup check `check_setup.py`, the made-up DemoKart data in `demo-data`, and its own rules in `CLAUDE.md`.

**Check it:** the tour mentions `support_agent/agent.py` and `check_setup.py`, and Claude Code says it changed nothing.

**If it went wrong:**

- *`claude` is not found:* close VS Code completely, open it again, and open a new terminal. VS Code only sees tools that were installed before it started.

**Explain it back:**
> What is CLAUDE.md, and why does this project have one? Answer in 3 short lines.

**Your brief:** the same for everyone.

---

## Step 4: Get a free Gemini key and put it in `.env`

**Why:** the agent's "brain" is Google's Gemini model. A key is like a password that lets your agent use it. The free key is enough for this course.

**Do this:**

1. Go to [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) and sign in with your Google account. Accept the terms if asked.
2. Click **Create API key**. If it asks for a project, let it create one for you.
3. Copy the key (it starts with `AIza`). Keep that browser tab open for now.

**Paste this into Claude Code:**
> Make a copy of .env.example called .env. Don't open or read .env afterwards.

**You should see:** a new file `.env` appears in VS Code's left panel. Claude Code says it made the copy.

**Then do this yourself:**

1. Click `.env` in VS Code's left panel to open it.
2. Find the line `GOOGLE_API_KEY=paste-your-key-here`.
3. Replace `paste-your-key-here` with your key. The line should look like `GOOGLE_API_KEY=AIza...` with no spaces and no quote marks.
4. Leave the `GEMINI_MODEL` line as it is.
5. Save the file: **Cmd+S** (Mac) or **Ctrl+S** (Windows).

**Check it:** `.env` is open in VS Code, the `GOOGLE_API_KEY` line holds your key, and the tab title shows no dot (a dot means unsaved changes). Step 6 tests that the key works.

**If it went wrong:**

- *AI Studio says the API isn't available:* some school or work Google accounts block AI Studio. Use a personal Google account.
- *You pasted the key into Claude Code by mistake:* go back to AI Studio, delete that key, make a new one, and put the new one in `.env`.

**Explain it back:**
> Without reading .env, explain in plain English what the .env file is for and why it must never be uploaded to GitHub.

**Your brief:** the same for everyone. Use your own key, not a friend's: each free key has its own daily limit.

---

## Step 5: Log in to GitHub from the terminal

**Why:** in Session 4 Claude Code puts your code on GitHub for you. It can only do that once you have logged in here. You do this once.

**Do this:** this login asks you questions, so you do it in a second terminal, not in Claude Code.

1. In VS Code's terminal panel, click the **+** button (top right of the panel) to open a second terminal.
2. Type this and press Enter:
   ```
   gh auth login
   ```
3. Answer the questions with the arrow keys and Enter:
   - Where do you use GitHub? **GitHub.com**
   - Preferred protocol? **HTTPS**
   - Authenticate Git with your GitHub credentials? **Yes**
   - How would you like to authenticate? **Login with a web browser**
4. It shows a one-time code like `ABCD-1234`. Copy it, press Enter, and a browser window opens. Paste the code, then click **Authorize**.
5. Back in the terminal you should see `Logged in as` and your GitHub username.

**Check it:** in the same second terminal, type `gh auth status`. It says `Logged in to github.com account` followed by your username.

**If it went wrong:**

- *No browser opens:* open [github.com/login/device](https://github.com/login/device) yourself and type the code there.

**Explain it back:** nothing to explain here. You can close this second terminal (click the bin icon), or keep it for Step 7.

**Your brief:** the same for everyone.

---

## Step 6: Set up the project and run the setup check

**Why:** the agent needs some Python packages. Claude Code installs them into a folder called `.venv` that belongs to this project only, then runs a check that tests everything, including your key.

**Paste this into Claude Code** (in the first terminal, where Claude Code is running):
> Set up this project for me: create a Python virtual environment in a folder called .venv using Python 3.13, install the packages from requirements.txt into it, then run check_setup.py with the .venv Python. Tell me the result in plain words.

**You should see:** Claude Code runs three things, asking permission for each the first time:

1. It creates `.venv` with Python 3.13 (a few seconds).
2. It installs the packages (2 to 5 minutes; this is the big download).
3. It runs the setup check and tells you what it says.

**Check it:** the setup check ends with **All OK. You are ready.** Every line above it starts with `OK`:

```
Setup check
-----------
  OK    Python 3.13.x
  OK    Running inside the project's virtual environment (.venv)
  OK    Packages installed: google-adk 2.15.0, python-dotenv 1.2.4, chromadb 1.5.9, streamlit 1.67.0
  OK    .env file found
  OK    Gemini key is filled in (not shown)
  OK    Model name set: gemini-3.5-flash-lite
  OK    Gemini replied using gemini-3.5-flash-lite ('OK')
  OK    git version ...
  OK    gh version ...
  OK    GitHub CLI is logged in

All OK. You are ready.
```

You can run the check again at any time:

- Mac: `.venv/bin/python check_setup.py`
- Windows: `.venv\Scripts\python check_setup.py` *(Windows, not tested by us)*

**If it went wrong:** every `FIX` line says what to do. The common ones:

- *"The Gemini key in .env is still empty":* you didn't save `.env` after pasting the key. Open it, check the line, press Cmd+S or Ctrl+S, and run the check again.
- *"Google says the key is not valid":* copy the key again from AI Studio. Check that there are no spaces or quote marks in the `.env` line.
- *"free limit is used up":* wait a minute and run the check again.
- *The package install fails and mentions "rustc", "Rust" or "building wheel":* your Python is not 3.13. Ask Claude Code: `Delete the .venv folder and create it again with Python 3.13, then install requirements.txt again.`
- *"CERTIFICATE_VERIFY_FAILED" (Mac):* open Finder, go to **Applications > Python 3.13**, and double-click **Install Certificates.command**. Then run the check again.
- *The install is very slow:* it downloads about 170 MB. On slow Wi-Fi it can take over 10 minutes. Let it finish.

**Explain it back:**
> In plain English, what is the .venv folder, and why does the project have its own one instead of using the Python on my laptop? 3 short lines.

**Your brief:** the same for everyone.

---

## Step 7: Start the agent and say "Hi"

**Why:** this is the agent you will build on. Today it only knows how to be friendly. In Session 1 you give it a job.

**Do this:** the agent's chat page runs in its own terminal, so Claude Code stays free.

1. Open a second terminal with the **+** button (or use the one from Step 5).
2. Paste the line for your system and press Enter:
   - Mac:
     ```
     .venv/bin/adk web
     ```
   - Windows *(Windows, not tested by us)*:
     ```
     .venv\Scripts\adk web
     ```
3. Wait for a box that says **ADK Web Server started**. Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
4. The first time, a box called **Help Improve ADK!** asks to collect usage data. Click **No Thanks**.
5. At the top left you see **support_agent**. That's your agent.
6. Type `Hi` in the **Type a message...** box at the bottom and press Enter.

**You should see:** your "Hi" on the right, and the agent's reply below it: a short, friendly greeting, such as "Hello! How can I help you today?"

**Check it:** the reply appears within a few seconds. Then stop the agent: click in the second terminal and press **Ctrl+C**. The terminal prompt comes back.

From now on, this is how you start and stop the agent's chat page. It does **not** pick up changes by itself: whenever Claude Code changes the agent, stop the chat page (**Ctrl+C**), press the **Up arrow** key to bring back the last command, and press **Enter** to start it again.

**If it went wrong:**

- *"address already in use" or port 8000 is busy:* another copy is already running, maybe in a terminal you forgot. Close the other terminals, or start this one on another port: add `--port 8001` to the end of the line and open `http://127.0.0.1:8001`.
- *The agent replies with an error about the API key:* run the setup check again (Step 6) and fix what it says.
- *"No such file or directory: .venv/bin/adk":* the terminal is not in the project folder, or Step 6 didn't finish. Make sure VS Code has the project folder open, open a new terminal, and try again.

**Explain it back** (in the Claude Code terminal):
> In plain English, what happens between me typing "Hi" in the chat page and the reply appearing? Point me to the lines in support_agent/agent.py that matter. Keep it short.

**Your brief:** the starter agent doesn't belong to any business yet. In Session 1 you give it your business's name, tone and rules.

---

## You're done when

- [ ] The setup check says **All OK. You are ready.**
- [ ] The starter agent replied to "Hi" in the chat page.

**Next:** open the Session 1 guide. You don't need to download anything new: keep working in this same folder. Read the guide on GitHub, in the `session-1` branch: [session1.md](https://github.com/abduljabbarpeer/customer-support-agent/blob/session-1/session1.md).
