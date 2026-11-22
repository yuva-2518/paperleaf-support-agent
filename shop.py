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
    "<span class='pl-chip'>🎁 Gift wrapping available</span></div>",
    unsafe_allow_html=True,
)

books = load_books()

# A few numbers about the shop, and a way into the chat.
pre_loved = sum(1 for b in books if b["condition"] == "Pre-loved")
st.markdown(
    f"<div class='pl-stats'>"
    f"<div class='pl-stat'><b>{len(books)}</b><span>books to browse</span></div>"
    f"<div class='pl-stat'><b>{len({b['category'] for b in books})}</b><span>categories</span></div>"
    f"<div class='pl-stat'><b>{pre_loved}</b><span>pre-loved finds</span></div>"
    f"<div class='pl-stat'><b>9 AM - 9 PM</b><span>support team, every day</span></div></div>",
    unsafe_allow_html=True,
)
st.page_link("app.py", label="Need help? Chat with Paige", icon="💬")

# Search and filters.
st.subheader("Browse our books")
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


def show_books(list_of_books):
    """The books, three to a row."""
    for start in range(0, len(list_of_books), 3):
        for column, book in zip(st.columns(3), list_of_books[start:start + 3]):
            column.markdown(book_card(book), unsafe_allow_html=True)


# With no search or filter, start with the top-rated books.
if not search and category == "All categories" and condition == "New and Pre-loved":
    st.markdown("##### ⭐ Top rated")
    show_books(sorted(books, key=lambda b: float(b["rating"]), reverse=True)[:3])
    st.markdown("##### All books")

st.caption(f"Showing {len(shown)} of {len(books)} books")
if not shown:
    st.warning("No books match your search. Try a different word or filter.")
show_books(shown)

st.markdown(
    "<div class='pl-footer'>PaperLeaf Books · Printed books across India · "
    "Support team available 9 AM to 9 PM, all days</div>",
    unsafe_allow_html=True,
)
