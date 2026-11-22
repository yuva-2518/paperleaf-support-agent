"""
The look of the PaperLeaf website: colours, fonts, cards and chat bubbles, in light or dark mode.

Every colour is a named variable (like --bg or --text). Dark mode simply swaps the values.
Both pages call apply_style() at the top. The Dark mode switch (website.py) sets
st.session_state["dark"].
"""

import streamlit as st

# The colours for each mode.
LIGHT = """
--bg:#FBF7F0; --side:#F3EADB; --card:#FFFFFF; --text:#2B2420; --muted:#6B5F57;
--border:#EADFCB; --border2:#E0D0B6; --accent:#8B2E3C; --title:#5A1A26; --soft:#F3EADB;
--input:#FFFFFF; --shadow:rgba(60,30,20,.08); --green-bg:#E3F0E4; --green:#1F5A2B;
--star:#B7791F; --avatar:#F3E3E5; --btn-text:#8B2E3C; --btn-hover-text:#FFFFFF;
"""
DARK = """
--bg:#15110F; --side:#1C1714; --card:#231D19; --text:#F1E9DF; --muted:#B9ACA0;
--border:#392F29; --border2:#4A3D34; --accent:#E08A9A; --title:#F2B8C2; --soft:#2E2621;
--input:#2A2320; --shadow:rgba(0,0,0,.45); --green-bg:#1F3A27; --green:#8FD3A1;
--star:#E5B84C; --avatar:#3A2428; --btn-text:#EBA3B0; --btn-hover-text:#1A0F12;
"""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&display=swap');
:root { __COLOURS__ }

/* ---------- Page, text and sidebar ---------- */
.stApp { background: var(--bg); color: var(--text); }
[data-testid="stHeader"] { background: transparent; }
.stApp p, .stApp li, .stApp label, .stApp h4, .stApp h5, .stApp h6,
[data-testid="stWidgetLabel"] p, [data-testid="stMarkdownContainer"] p { color: var(--text); }
.stApp h1, .stApp h2, .stApp h3, .pl-serif { font-family: 'Playfair Display', Georgia, serif !important; letter-spacing: .2px; color: var(--title); }
[data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] p { color: var(--muted); }
.block-container { padding-top: 2rem; max-width: 1100px; }
footer, #MainMenu { visibility: hidden; }
hr { border-color: var(--border) !important; }

[data-testid="stSidebar"] { background: var(--side); border-right: 1px solid var(--border2); }
[data-testid="stSidebarNavLink"] span { color: var(--text); }
[data-testid="stSidebarNavLink"][aria-current="page"] { background: var(--border); }
[data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 { color: var(--title); }

/* ---------- Buttons ---------- */
.stButton > button, .stFormSubmitButton > button, [data-testid="stPageLink-NavLink"] {
  border-radius: 999px; border: 1px solid var(--accent); color: var(--btn-text); background: var(--card);
  font-weight: 600; transition: all .15s ease;
}
.stButton > button p, .stFormSubmitButton > button p { color: inherit !important; }
[data-testid="stPageLink-NavLink"], [data-testid="stPageLink-NavLink"] * { color: var(--btn-text) !important; }
[data-testid="stPageLink-NavLink"]:hover, [data-testid="stPageLink-NavLink"]:hover * { color: var(--btn-hover-text) !important; }
.stButton > button:hover, .stFormSubmitButton > button:hover, [data-testid="stPageLink-NavLink"]:hover {
  background: var(--accent); color: var(--btn-hover-text); border-color: var(--accent);
}

/* ---------- Inputs ---------- */
[data-testid="stTextInputRootElement"], [data-testid="stTextAreaRootElement"], [data-testid="stNumberInputContainer"],
[data-testid="stSelectbox"] [role="group"] {
  background: var(--input) !important; border: 1px solid var(--border2) !important; border-radius: 10px !important;
}
[data-testid="stSelectbox"] button, [data-testid="stSelectbox"] svg { color: var(--muted) !important; fill: var(--muted) !important; }
[data-testid="stSelectbox"] input { color: var(--text) !important; }
.react-aria-Popover, [role="listbox"], [data-testid="stSelectboxVirtualDropdown"] { background: var(--card) !important; color: var(--text) !important; border-radius: 10px; }
[role="option"], [role="option"] * { color: var(--text) !important; background: transparent; }
[role="option"][data-focused="true"], [role="option"]:hover { background: var(--soft) !important; }

[data-baseweb="input"], [data-baseweb="base-input"], [data-baseweb="textarea"], [data-baseweb="select"] > div {
  background: var(--input) !important; border-color: var(--border2) !important; border-radius: 10px;
}
input, textarea { color: var(--text) !important; -webkit-text-fill-color: var(--text) !important; }
input::placeholder, textarea::placeholder { color: var(--muted) !important; -webkit-text-fill-color: var(--muted) !important; opacity: .85; }
[data-baseweb="select"] div, [data-baseweb="select"] span { color: var(--text); }
[data-baseweb="select"] svg { fill: var(--muted); }
[data-baseweb="popover"] [data-baseweb="menu"], [data-baseweb="popover"] ul { background: var(--card) !important; }
[data-baseweb="popover"] li, [data-baseweb="popover"] li div { color: var(--text) !important; }
[data-baseweb="popover"] li:hover { background: var(--soft) !important; }
[data-testid="stForm"] { background: var(--card); border: 1px solid var(--border2); border-radius: 16px; padding: 1.2rem; }
[data-testid="stAlert"] { background: var(--card); border: 1px solid var(--border2); border-radius: 12px; }
[data-testid="stAlert"] p { color: var(--text); }

/* ---------- Home page ---------- */
.pl-hero {
  background: linear-gradient(120deg, #5A1A26 0%, #8B2E3C 55%, #B5586A 100%);
  border-radius: 20px; padding: 2.2rem 2rem; margin-bottom: 1rem;
}
.pl-hero h1 { color: #fff !important; margin: 0 0 .3rem 0; font-size: 2.4rem; }
.pl-hero p { color: #fff !important; margin: 0 0 1rem 0; font-size: 1.1rem; opacity: .92; }
.pl-chip {
  display: inline-block; background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.35);
  border-radius: 999px; padding: .3rem .85rem; margin: 0 .5rem .4rem 0; font-size: .9rem; color: #fff !important;
}
.pl-stats { display: flex; gap: .8rem; margin: .4rem 0 1.4rem 0; flex-wrap: wrap; }
.pl-stat { flex: 1; min-width: 140px; background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: .8rem 1rem; text-align: center; }
.pl-stat b { display: block; font-family: 'Playfair Display', Georgia, serif; font-size: 1.5rem; color: var(--accent); }
.pl-stat span { font-size: .85rem; color: var(--muted); }
.pl-footer { text-align: center; color: var(--muted); font-size: .85rem; margin: 2rem 0 .5rem 0; padding-top: 1rem; border-top: 1px solid var(--border); }

/* ---------- Book cards ---------- */
.pl-card {
  background: var(--card); border: 1px solid var(--border); border-radius: 16px; overflow: hidden;
  margin-bottom: 1.1rem; box-shadow: 0 2px 8px var(--shadow); transition: transform .15s ease, box-shadow .15s ease;
}
.pl-card:hover { transform: translateY(-3px); box-shadow: 0 8px 18px var(--shadow); }
.pl-cover {
  min-height: 150px; padding: 1.2rem 1rem; display: flex; flex-direction: column; justify-content: center;
  align-items: center; text-align: center; color: #fff; border-left: 12px solid rgba(0,0,0,.22);
}
.pl-cover .pl-cover-title { font-family: 'Playfair Display', Georgia, serif; font-size: 1.2rem; font-weight: 700; line-height: 1.25; }
.pl-cover .pl-cover-author { margin-top: .5rem; font-size: .85rem; opacity: .9; }
.pl-body { padding: .9rem 1rem 1rem 1rem; }
.pl-tags { margin-bottom: .5rem; }
.pl-tag { display: inline-block; font-size: .72rem; font-weight: 600; border-radius: 999px; padding: .15rem .6rem; margin-right: .35rem; background: var(--soft); color: var(--title); }
.pl-tag.pre { background: var(--green-bg); color: var(--green); }
.pl-desc { font-size: .9rem; color: var(--muted); min-height: 4.2em; margin: 0 0 .7rem 0; }
.pl-foot { display: flex; justify-content: space-between; align-items: center; }
.pl-price { font-family: 'Playfair Display', Georgia, serif; font-size: 1.4rem; font-weight: 700; color: var(--accent); }
.pl-rating { font-size: .9rem; color: var(--star); font-weight: 600; }

/* ---------- Customer service page ---------- */
.pl-chat-head {
  display: flex; align-items: center; gap: .9rem; background: var(--card); border: 1px solid var(--border);
  border-radius: 16px; padding: .8rem 1.1rem; box-shadow: 0 2px 8px var(--shadow);
}
.pl-avatar { width: 46px; height: 46px; border-radius: 50%; background: var(--avatar); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; }
.pl-chat-name { font-family: 'Playfair Display', Georgia, serif; font-size: 1.25rem; font-weight: 700; color: var(--title); }
.pl-chat-sub { font-size: .85rem; color: var(--muted); }
.pl-dot { display: inline-block; width: 9px; height: 9px; border-radius: 50%; background: #2E9E5B; margin-right: .3rem; }
.pl-hours { margin-left: auto; font-size: .8rem; color: var(--muted); text-align: right; }
.pl-topics { margin: .7rem 0 1.1rem 0; font-size: .92rem; color: var(--muted); }
.pl-start-title { font-family: 'Playfair Display', Georgia, serif; font-size: 1.05rem; color: var(--title); margin: 1rem 0 .5rem 0; }

/* Chat bubbles: the customer's on the right (no face icon), Paige's on the left */
[data-testid="stChatMessage"] { border-radius: 18px; padding: .9rem 1.1rem; margin-bottom: .6rem; background: var(--card); border: 1px solid var(--border); }
[data-testid="stChatMessage"] p, [data-testid="stChatMessage"] li { color: var(--text); }
[data-testid="stChatMessage"]:has([aria-label="Chat message from user"]) {
  flex-direction: row-reverse; margin-left: auto; width: fit-content; max-width: 85%;
  background: #8B2E3C; border-color: #8B2E3C;
}
[data-testid="stChatMessage"]:has([aria-label="Chat message from user"]) > div:first-child { display: none; }
[data-testid="stChatMessage"]:has([aria-label="Chat message from user"]) * { color: #fff !important; }
[data-testid="stChatMessage"]:has([aria-label="Chat message from assistant"]) { max-width: 92%; width: fit-content; }

/* The message box at the bottom */
[data-testid="stChatInput"] > div { background: var(--card); border: 1px solid var(--border2); border-radius: 26px; box-shadow: 0 2px 8px var(--shadow); }
[data-testid="stChatInput"] textarea { background: transparent !important; }
[data-testid="stChatInput"] { max-width: 660px; margin-left: auto; margin-right: auto; }
[data-testid="stChatInput"] button { background: transparent !important; color: var(--accent) !important; }
[data-testid="stChatMessage"] > div:first-child { background: var(--avatar) !important; border: 1px solid var(--border) !important; }
[data-testid="stBottom"] > div { background: var(--bg); }

/* Topic cards at the start of a chat, and small quick-reply chips */
.st-key-topics .stButton > button { height: 64px; border-radius: 14px; font-size: 1rem; }
.st-key-quick .stButton > button { padding: .35rem .6rem; font-size: .9rem; }

/* Tickets in the sidebar */
.pl-ticket { background: var(--card); border: 1px solid var(--border2); border-radius: 12px; padding: .7rem .8rem; margin-bottom: .6rem; }
.pl-ticket-id { font-weight: 700; color: var(--accent); }
.pl-ticket-status { float: right; font-size: .72rem; font-weight: 600; background: var(--green-bg); color: var(--green); border-radius: 999px; padding: .1rem .55rem; }
.pl-ticket-reason { margin-top: .3rem; font-size: .9rem; color: var(--text); }
.pl-ticket-time { margin-top: .2rem; font-size: .75rem; color: var(--muted); }

/* Passcode screen */
.pl-lock { text-align: center; margin: 2rem 0 1rem 0; }
.pl-lock-icon { font-size: 2.6rem; }
.pl-lock-title { font-family: 'Playfair Display', Georgia, serif; font-size: 1.5rem; font-weight: 700; color: var(--title); margin-top: .3rem; }
.pl-lock-text { color: var(--muted); margin-top: .2rem; }
</style>
"""


def apply_style():
    """Add the website's look to the current page, in light or dark mode."""
    colours = DARK if st.session_state.get("dark") else LIGHT
    st.markdown(CSS.replace("__COLOURS__", colours), unsafe_allow_html=True)
