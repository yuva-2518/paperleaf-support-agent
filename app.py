"""
The customer chat page for Paige, made with Streamlit.

It talks to the same Paige as adk web. The difference: when Paige needs details,
customers get a real form with typing boxes and a Send button.

Run it with:  .venv/Scripts/streamlit run app.py   (Mac: .venv/bin/streamlit run app.py)

Settings:
- On your laptop, the Gemini key and model come from .env (as for adk web).
- When deployed on Streamlit Community Cloud, they come from the app's Secrets.
- APP_PASSCODE (the passcode to open the chat) always comes from Streamlit secrets:
  on your laptop that is the file .streamlit/secrets.toml.
"""

import asyncio
import hmac
import os
import uuid

import streamlit as st

# When deployed, copy the Gemini key and model from Streamlit secrets so Paige can find them.
# On your laptop there may be no secrets for these, and Paige reads .env instead.
# (This must run BEFORE Paige is loaded below, because she reads the settings when she starts.)
for setting in ("GOOGLE_API_KEY", "GEMINI_MODEL"):
    try:
        if setting in st.secrets:
            os.environ[setting] = st.secrets[setting]
    except Exception:
        pass  # no secrets file at all: fine on a laptop

from google.adk.runners import InMemoryRunner  # noqa: E402
from google.genai import types  # noqa: E402

from support_agent.agent import CHAT_NOTES, DETAILS_FORM, SORRY_MESSAGE, read_tickets, root_agent  # noqa: E402

GREETING = "Hello, I'm Paige from PaperLeaf Books. How can I help you today?"

# The first line of the details form. If Paige's reply contains it, we show the real form instead.
FORM_START = DETAILS_FORM.splitlines()[0]


@st.cache_resource
def get_runner():
    """Start Paige once and share her between page refreshes."""
    return InMemoryRunner(agent=root_agent, app_name="paperleaf")


def ask_paige(text):
    """Send the customer's message to Paige and return her reply."""
    reply = ""
    try:
        for event in get_runner().run(
            user_id=st.session_state.user_id,
            session_id=st.session_state.session_id,
            new_message=types.Content(role="user", parts=[types.Part(text=text)]),
        ):
            if event.is_final_response() and event.content and event.content.parts:
                reply = "".join(part.text or "" for part in event.content.parts)
    except Exception as error:
        print(f"[Paige] error: {error}")  # for you, in the terminal; the customer sees a kind message
        reply = SORRY_MESSAGE
    return reply.strip() or SORRY_MESSAGE


def send(text):
    """Add the customer's message, get Paige's reply, and spot if she sent the form."""
    st.session_state.messages.append({"role": "user", "content": text, "form": False})
    with st.spinner("Paige is typing..."):
        reply = ask_paige(text)
    has_form = FORM_START in reply
    if has_form:
        # Keep only Paige's words before the form; the real form is shown below them.
        reply = reply.split(FORM_START)[0].strip() or "Please fill in this form."
    st.session_state.messages.append({"role": "assistant", "content": reply, "form": has_form})


def field(title, widget, **options):
    """Show a bold title, with its input box right below it."""
    st.markdown(f"**{title}**")
    return widget(title, label_visibility="collapsed", **options)


def show_details_form(key):
    """The real form: a bordered box with a title and an input below it for each detail."""
    with st.form(key, border=True):
        st.subheader("Your details")
        st.caption("Leave blank anything that doesn't apply. Never share card numbers, OTPs or passwords.")
        answers = {
            "Order ID": field("1. Order ID", st.text_input),
            "Book title": field("2. Book title", st.text_input),
            "What happened": field(
                "3. What happened (what is damaged, wrong or the problem)", st.text_area
            ),
            "Amount (₹)": field("4. Amount (₹)", st.text_input),
            "Email or phone on your PaperLeaf account": field(
                "5. Email or phone on your PaperLeaf account", st.text_input
            ),
        }
        submitted = st.form_submit_button("Send details")
    if submitted:
        # Turn the filled boxes into one message for Paige, skipping empty ones.
        lines = [f"{title}: {value.strip()}" for title, value in answers.items() if value.strip()]
        send("\n".join(lines) or "I left the form blank.")
        st.rerun()


def check_passcode():
    """Show a passcode box. The chat opens only after the right passcode is entered."""
    if st.session_state.get("unlocked"):
        return
    try:
        passcode = st.secrets["APP_PASSCODE"]
    except Exception:
        st.error("The passcode is not set up yet. Add APP_PASSCODE to the app's secrets.")
        st.stop()

    with st.form("passcode_form"):
        entered = st.text_input("Please enter the passcode to start chatting", type="password")
        if st.form_submit_button("Open chat"):
            # compare_digest compares safely, so the passcode can't be guessed by timing.
            if hmac.compare_digest(entered.encode(), str(passcode).encode()):
                st.session_state.unlocked = True
                st.rerun()
            st.error("Sorry, that passcode isn't right. Please try again.")
    st.stop()  # don't show the chat until the passcode is right


def show_sidebar():
    """Show this chat's open tickets. Never other customers' tickets."""
    with st.sidebar:
        # A new chat is a fresh session with Paige (it needs the passcode only once).
        if st.button("Start a new chat", use_container_width=True):
            for key in ("session_id", "user_id", "messages"):
                st.session_state.pop(key, None)
            st.rerun()
        st.header("Your open tickets")
        my_ids = CHAT_NOTES.get(st.session_state.session_id, {}).get("ticket_ids", [])
        mine = [t for t in read_tickets() if t["ticket_id"] in my_ids and t["status"] == "open"]
        if not mine:
            st.caption("No open tickets in this chat yet.")
        for ticket in mine:
            st.markdown(
                f"**{ticket['ticket_id']}**  \n{ticket['reason']}  \n"
                f"_{ticket['time'].replace('T', ' ')} · {ticket['status']}_"
            )


# --- The page ---
st.set_page_config(page_title="PaperLeaf Books Support", page_icon="📚")
from style import apply_style  # noqa: E402

apply_style()
st.title("PaperLeaf Books Support")
st.caption("💬 Chat with Paige about your books, orders, delivery, payments, returns and refunds.")
check_passcode()

# A new visitor gets their own private chat with Paige (one customer never sees another's).
if "session_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())
    session = asyncio.run(
        get_runner().session_service.create_session(
            app_name="paperleaf",
            user_id=st.session_state.user_id,
            state={"form_page": True},  # tells Paige this page shows a real form
        )
    )
    st.session_state.session_id = session.id
    st.session_state.messages = [{"role": "assistant", "content": GREETING, "form": False}]

show_sidebar()

# Show the chat so far. The form appears only under Paige's latest message.
messages = st.session_state.messages
for i, message in enumerate(messages):
    with st.chat_message(message["role"], avatar="📖" if message["role"] == "assistant" else "🙂"):
        st.markdown(message["content"].replace("\n", "  \n"))  # keep line breaks
        if message["form"] and i == len(messages) - 1:
            show_details_form(key=f"details_form_{i}")

def quick_replies():
    """Tap-to-reply buttons under Paige's latest message (they send a normal message)."""
    last = messages[-1]
    if last["role"] != "assistant" or last["form"]:
        return
    text = last["content"].lower()

    if len(messages) == 1:  # the start of the chat: common topics
        options = [
            ("🚚 Delivery", "How long does delivery take?"),
            ("💳 Payments", "Which payment methods can I use?"),
            ("↩️ Returns", "What is your return policy?"),
            ("📦 Track my order", "How do I track my order?"),
        ]
    elif "1 to 5 stars" in text:  # the rating question
        options = [(f"{n} ⭐", str(n)) for n in range(1, 6)]
    elif "resolved" in text:
        options = [("Yes, it's resolved", "Yes, it's resolved, thank you."), ("No, not yet", "No, it's not resolved yet.")]
    elif text.rstrip().endswith("?") and any(
        start in text for start in ("shall i", "would you like", "is that right", "do you want")
    ):
        options = [("Yes", "Yes"), ("No", "No")]
    else:
        return

    columns = st.columns(len(options))
    for column, (label, message) in zip(columns, options):
        if column.button(label, key=f"quick_{len(messages)}_{label}", use_container_width=True):
            send(message)
            st.rerun()


quick_replies()

# The message box at the bottom.
if text := st.chat_input("Type your message"):
    send(text)
    st.rerun()
