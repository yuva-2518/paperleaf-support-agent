"""
The look of the PaperLeaf website (colours, fonts, cards, chat bubbles).
Both pages call apply_style() once at the top.
"""

import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&display=swap');

/* Headings in a bookish serif font */
h1, h2, h3, .pl-serif { font-family: 'Playfair Display', Georgia, serif !important; letter-spacing: 0.2px; }
h1 { color: #5A1A26; }

/* Tidy the page: less empty space on top, no footer */
.block-container { padding-top: 2rem; max-width: 1100px; }
footer, #MainMenu { visibility: hidden; }

/* Sidebar */
[data-testid="stSidebar"] { background: #F3EADB; border-right: 1px solid #E4D6BF; }

/* Buttons */
.stButton > button, .stFormSubmitButton > button {
  border-radius: 999px; border: 1px solid #8B2E3C; color: #8B2E3C; background: #fff;
  font-weight: 600; transition: all .15s ease;
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
  background: #8B2E3C; color: #fff; border-color: #8B2E3C;
}

/* Boxes: forms and input fields */
[data-testid="stForm"] { background: #fff; border: 1px solid #E4D6BF; border-radius: 16px; padding: 1.2rem; }
.stTextInput input, .stTextArea textarea, .stSelectbox [data-baseweb="select"] > div {
  border-radius: 10px;
}

/* Chat bubbles */
[data-testid="stChatMessage"] { border-radius: 18px; padding: 0.9rem 1.1rem; margin-bottom: 0.6rem; background: #fff; border: 1px solid #EADFCB; }
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) { background: #F3E3E5; border-color: #E8CDD1; }
[data-testid="stChatInput"] { border-radius: 16px; }

/* Home page banner */
.pl-hero {
  background: linear-gradient(120deg, #5A1A26 0%, #8B2E3C 55%, #B5586A 100%);
  color: #fff; border-radius: 20px; padding: 2.2rem 2rem; margin-bottom: 1.2rem;
}
.pl-hero h1 { color: #fff; margin: 0 0 .3rem 0; font-size: 2.4rem; }
.pl-hero p { margin: 0 0 1rem 0; font-size: 1.1rem; opacity: .92; }
.pl-chip {
  display: inline-block; background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.35);
  border-radius: 999px; padding: .3rem .85rem; margin: 0 .5rem .4rem 0; font-size: .9rem;
}

/* Book cards */
.pl-card {
  background: #fff; border: 1px solid #EADFCB; border-radius: 16px; overflow: hidden;
  margin-bottom: 1.1rem; box-shadow: 0 2px 8px rgba(60,30,20,.06);
  transition: transform .15s ease, box-shadow .15s ease;
}
.pl-card:hover { transform: translateY(-3px); box-shadow: 0 8px 18px rgba(60,30,20,.12); }
.pl-cover {
  min-height: 150px; padding: 1.2rem 1rem; display: flex; flex-direction: column; justify-content: center;
  align-items: center; text-align: center; color: #fff; border-left: 12px solid rgba(0,0,0,.22);
}
.pl-cover .pl-cover-title { font-family: 'Playfair Display', Georgia, serif; font-size: 1.2rem; font-weight: 700; line-height: 1.25; }
.pl-cover .pl-cover-author { margin-top: .5rem; font-size: .85rem; opacity: .9; }
.pl-body { padding: .9rem 1rem 1rem 1rem; }
.pl-tags { margin-bottom: .5rem; }
.pl-tag { display: inline-block; font-size: .72rem; font-weight: 600; border-radius: 999px; padding: .15rem .6rem; margin-right: .35rem; background: #F3EADB; color: #5A1A26; }
.pl-tag.pre { background: #E3F0E4; color: #1F5A2B; }
.pl-desc { font-size: .9rem; color: #4A3F39; min-height: 4.2em; margin: 0 0 .7rem 0; }
.pl-foot { display: flex; justify-content: space-between; align-items: center; }
.pl-price { font-family: 'Playfair Display', Georgia, serif; font-size: 1.4rem; font-weight: 700; color: #8B2E3C; }
.pl-rating { font-size: .9rem; color: #B7791F; font-weight: 600; }
</style>
"""


def apply_style():
    """Add the website's look to the current page."""
    st.markdown(CSS, unsafe_allow_html=True)
