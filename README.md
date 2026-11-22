# Build a customer-support agent with Claude Code

In these sessions you build an AI customer-support agent for a business, **without writing code yourself**: you ask Claude Code, test what it built, and fix it by asking again.

The example business in the guides is **DemoKart**, a made-up online shop. You follow the same steps for the business in your own brief.

## You are on: `main` (the starter kit)

This branch holds the starter kit and the setup guide. Start here.

**Open the guide:** [session0.md](session0.md)

## All sessions

Each session lives on its own branch. A branch holds that session's guide and the finished code for the DemoKart example at the end of that session.

| Session | What you build | Guide | Download the code (ZIP) |
|---|---|---|---|
| 0. Setup | Tools, starter kit, Gemini key | [session0.md](https://github.com/abduljabbarpeer/customer-support-agent/blob/main/session0.md) | [main.zip](https://github.com/abduljabbarpeer/customer-support-agent/archive/refs/heads/main.zip) |
| 1. Give the agent a job | Name, tone and rules | [session1.md](https://github.com/abduljabbarpeer/customer-support-agent/blob/session-1/session1.md) | [session-1.zip](https://github.com/abduljabbarpeer/customer-support-agent/archive/refs/heads/session-1.zip) |
| 2. Knowledge from a Google Sheet | The agent answers from an FAQ Sheet | [session2-sheet.md](https://github.com/abduljabbarpeer/customer-support-agent/blob/session-2-sheet/session2-sheet.md) | [session-2-sheet.zip](https://github.com/abduljabbarpeer/customer-support-agent/archive/refs/heads/session-2-sheet.zip) |
| 2. Knowledge from help docs | The agent searches help documents | [session2-rag.md](https://github.com/abduljabbarpeer/customer-support-agent/blob/session-2-rag/session2-rag.md) | [session-2-rag.zip](https://github.com/abduljabbarpeer/customer-support-agent/archive/refs/heads/session-2-rag.zip) |
| 3. Hand-off and guardrails | Tickets for a human, safety rules | [session3.md](https://github.com/abduljabbarpeer/customer-support-agent/blob/session-3/session3.md) | [session-3.zip](https://github.com/abduljabbarpeer/customer-support-agent/archive/refs/heads/session-3.zip) |
| 4. Go live | A chat page, on GitHub and online | [session4.md](https://github.com/abduljabbarpeer/customer-support-agent/blob/session-4/session4.md) | [session-4.zip](https://github.com/abduljabbarpeer/customer-support-agent/archive/refs/heads/session-4.zip) |

**Session 2 has two tracks.** If your brief gives you a Google Sheet of FAQs, follow the Google Sheet guide. If your brief gives you help documents, follow the help-docs guide. Do one, not both.

## Fell behind?

You can continue from where the DemoKart example ended any session:

1. Download the ZIP of the session before the one you are starting, from the table above, and unzip it.
2. Copy your `.env` file from your old project folder into the new folder.
3. Open the new folder in VS Code, start Claude Code, and do [Step 6 of the setup guide](session0.md#step-6-set-up-the-project-and-run-the-setup-check) again (it rebuilds `.venv`).

## Keep your key safe

Your Gemini key goes in the `.env` file only. Never paste it into Claude Code, into code, or anywhere online. `.env` is listed in `.gitignore`, so Git never uploads it.
