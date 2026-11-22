"""
The PaperLeaf Books website: a login page, then a shop page and a Customer service page with Paige.

Run it with:  .venv/Scripts/streamlit run website.py   (Mac: .venv/bin/streamlit run website.py)

- Login (login.py): visitors enter the passcode first. Nothing else opens until they do.
- Shop (shop.py): the books from books.csv.
- Customer service (app.py): Paige's chat.
"""

import streamlit as st

from style import apply_style

st.set_page_config(page_title="PaperLeaf Books", page_icon="📚", layout="wide")
apply_style()

logged_in = st.session_state.get("unlocked", False)

if logged_in:
    pages = [
        st.Page("shop.py", title="Shop", icon="📚", default=True),
        st.Page("app.py", title="Customer service", icon="💬", url_path="customer-service"),
    ]
else:
    # Before the passcode, the only page is Login (and its menu is hidden).
    pages = [st.Page("login.py", title="Login", icon="🔒", url_path="login", default=True)]

page = st.navigation(pages, position="sidebar" if logged_in else "hidden")

# The Dark mode switch sits in the sidebar. Flipping it re-runs the page in the new colours.
st.sidebar.toggle("🌙 Dark mode", key="dark")

# Log out: forget the passcode and this chat, then show the Login page again.
if logged_in and st.sidebar.button("Log out", use_container_width=True):
    for key in ("unlocked", "session_id", "user_id", "messages"):
        st.session_state.pop(key, None)
    st.rerun()

page.run()
