"""
The login page of the PaperLeaf Books website: visitors enter the passcode here.

The passcode (APP_PASSCODE) comes from Streamlit secrets: on your laptop that is the file
.streamlit/secrets.toml. After the right passcode, the Shop and Customer service open.
"""

import hmac

import streamlit as st


def login_screen():
    """Show the passcode card. When the passcode is right, unlock the site and reload."""
    try:
        passcode = st.secrets["APP_PASSCODE"]
    except Exception:
        st.error("The passcode is not set up yet. Add APP_PASSCODE to the app's secrets.")
        return

    _, middle, _ = st.columns([1, 2, 1])  # centre the card
    with middle:
        st.markdown(
            "<div class='pl-lock'><div class='pl-lock-icon'>📚</div>"
            "<div class='pl-lock-title'>Welcome to PaperLeaf Books</div>"
            "<div class='pl-lock-text'>Please log in with the passcode to continue.</div></div>",
            unsafe_allow_html=True,
        )
        with st.form("login_form"):
            entered = st.text_input("Passcode", type="password", placeholder="Enter your passcode")
            if st.form_submit_button("Log in", use_container_width=True):
                # compare_digest compares safely, so the passcode can't be guessed by timing.
                if hmac.compare_digest(entered.encode(), str(passcode).encode()):
                    st.session_state.unlocked = True
                    st.rerun()
                st.error("Sorry, that passcode isn't right. Please try again.")


# When this file runs as the Login page, show the login card.
if __name__ == "__main__":
    login_screen()
