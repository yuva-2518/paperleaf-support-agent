"""
The PaperLeaf Books website: a shop page and a Customer service page with Paige.

Run it with:  .venv/Scripts/streamlit run website.py   (Mac: .venv/bin/streamlit run website.py)

- Shop (shop.py): the books from books.csv. Anyone can look.
- Customer service (app.py): Paige's chat, behind the passcode, exactly as before.
"""

import streamlit as st

from style import apply_style

st.set_page_config(page_title="PaperLeaf Books", page_icon="📚", layout="wide")
apply_style()

pages = [
    st.Page("shop.py", title="Shop", icon="📚", default=True),
    st.Page("app.py", title="Customer service", icon="💬", url_path="customer-service"),
]
page = st.navigation(pages)

# The Dark mode switch sits in the sidebar, under the menu. Flipping it re-runs the page in the new colours.
st.sidebar.toggle("🌙 Dark mode", key="dark")

page.run()
