"""
The shop page of the PaperLeaf Books website: shows the books from books.csv.
(It is a page inside website.py. The customer-service chat is the other page.)
"""

import csv
import html
import os

import streamlit as st

BOOKS_FILE = os.path.join(os.path.dirname(__file__), "books.csv")

# One cover colour per category, so the page feels like a bookshop.
CATEGORY_COLOURS = {
    "Fiction": "#7B5AA6", "Mystery": "#2F4B73", "Science Fiction": "#1F8A7E",
    "Self-help": "#C98A1B", "Cooking": "#B84A33", "Children": "#D2567F", "History": "#5E634B",
}


@st.cache_data
def load_books():
    """Read the books from books.csv."""
    with open(BOOKS_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def book_card(book):
    """One book card as HTML: a coloured cover, tags, a short description, price and rating."""
    e = {key: html.escape(value) for key, value in book.items()}  # make text safe for the page
    colour = CATEGORY_COLOURS.get(book["category"], "#555555")
    condition_class = "pl-tag pre" if book["condition"] == "Pre-loved" else "pl-tag"
    return (
        f"<div class='pl-card'>"
        f"<div class='pl-cover' style='background:linear-gradient(135deg,{colour},{colour}CC 60%,#00000055)'>"
        f"<div class='pl-cover-title'>{e['title']}</div>"
        f"<div class='pl-cover-author'>by {e['author']}</div></div>"
        f"<div class='pl-body'>"
        f"<div class='pl-tags'><span class='pl-tag'>{e['category']}</span>"
        f"<span class='{condition_class}'>{e['condition']}</span></div>"
        f"<p class='pl-desc'>{e['description']}</p>"
        f"<div class='pl-foot'><span class='pl-price'>₹{e['price']}</span>"
        f"<span class='pl-rating'>★ {e['rating']}</span></div>"
        f"</div></div>"
    )


# The banner at the top.
st.markdown(
    "<div class='pl-hero'><h1>📚 PaperLeaf Books</h1>"
    "<p>Printed books, new and pre-loved, delivered across India.</p>"
    "<span class='pl-chip'>🚚 Free delivery above ₹499</span>"
    "<span class='pl-chip'>📖 New &amp; Pre-loved</span>"
    "<span class='pl-chip'>💬 Chat with Paige in Customer service</span></div>",
    unsafe_allow_html=True,
)

books = load_books()

# Search and filters.
left, middle, right = st.columns([2, 1, 1])
search = left.text_input("Search", placeholder="Search by title or author", label_visibility="collapsed")
category = middle.selectbox("Category", ["All categories"] + sorted({b["category"] for b in books}), label_visibility="collapsed")
condition = right.selectbox("Condition", ["New and Pre-loved", "New", "Pre-loved"], label_visibility="collapsed")

shown = [
    b for b in books
    if (search.lower() in b["title"].lower() or search.lower() in b["author"].lower())
    and (category == "All categories" or b["category"] == category)
    and (condition == "New and Pre-loved" or b["condition"] == condition)
]

st.caption(f"Showing {len(shown)} of {len(books)} books")
if not shown:
    st.warning("No books match your search. Try a different word or filter.")

# The books, three to a row.
for start in range(0, len(shown), 3):
    columns = st.columns(3)
    for column, book in zip(columns, shown[start:start + 3]):
        column.markdown(book_card(book), unsafe_allow_html=True)
