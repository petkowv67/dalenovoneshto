import streamlit as st

st.title("📚 Приложение за книги")

# Създаваме списък, ако не съществува
if "books" not in st.session_state:
    st.session_state.books = []

# =====================================
# ➕ Добавяне на книга
# =====================================
st.header("➕ Добави книга")

title = st.text_input("Заглавие")
author = st.text_input("Автор")
price = st.number_input("Цена", min_value=0.0)

if st.button("Добави книгата"):
    if title and author:
        book = {
            "title": title,
            "author": author,
            "price": price
        }

        st.session_state.books.append(book)
        st.success("Книгата е добавена!")
    else:
        st.warning("Моля, попълнете всички полета.")

# =====================================
# 📚 Показване на всички книги
# =====================================
st.header("📚 Покажи всички книги")

if st.button("Покажи всички книги"):
    if len(st.session_state.books) == 0:
        st.write("Няма добавени книги.")
    else:
        for book in st.session_state.books:
            st.write("Заглавие:", book["title"])
            st.write("Автор:", book["author"])
            st.write("Цена:", f"{book['price']:.2f} euro.")
            st.write("----------------------")

# =====================================
# 🔎 Търсене по заглавие и цена
# =====================================
st.header("🔎 Търсене по заглавие и цена")

search_title = st.text_input("Въведи заглавие")
search_price = st.number_input("Въведи цена", min_value=0.0, value=0.0)

if st.button("Търси"):
    found = False

    for book in st.session_state.books:
        if (
            book["title"].lower() == search_title.lower()
            and book["price"] == search_price
        ):
            st.write("Заглавие:", book["title"])
            st.write("Автор:", book["author"])
            st.write("Цена:", f"{book['price']:.2f} euro.")
            st.write("----------------------")
            found = True

    if not found:
        st.write("Няма намерена книга с това заглавие и цена.")
# =========================
# 🔎 Търсене по автор
# =========================

st.header("🔎 Търсене по автор")

search_author = st.text_input("Въведи име на автор")

if st.button("Търси по автор"):

    found = False

    for book in st.session_state.books:
        if book["author"] == search_author:
            st.write(book)
            found = True

    if not found:
        st.write("Няма намерени книги от този автор.")
