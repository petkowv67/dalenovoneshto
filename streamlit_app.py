import streamlit as st

st.title("Приложение")

# Създаваме масив (списък), ако още не съществува
if "books" not in st.session_state:
    st.session_state.books = []

# =========================
# ➕ Добавяне на книга
# =========================
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

# =========================
# 📚 Списък с книги
# =========================
st.header("📚 Налични книги")

if st.session_state.books:
    for i, book in enumerate(st.session_state.books, 1):
        st.write(f"{i}. {book['title']} - {book['author']} - {book['price']:.2f} лв.")
else:
    st.info("Няма добавени книги все още.")
