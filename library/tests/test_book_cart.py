from dataclasses import dataclass
from library import book_cart
import pytest
from library.book_cart import Books_Cart
from library.books import Book

@pytest.fixture
def b_cart():
    database = "./tests/test_database.json"
    bcart = Books_Cart(database)
    bcart.empty_book_cart()
    return bcart

def test_empty_book_cart(b_cart):
    new_book = Book("a", "b", "comedy", 1.2)
    b_cart.retrieve_books(new_book)
    b_cart.empty_book_cart()
    assert len(b_cart.get_all_books()["Books"].items()) == 0

def test_search_books(b_cart):
    new_book = Book("rand", "Margie", "comedy", 0.2)
    b_cart.retrieve_books(new_book)
    book_list = b_cart.search_books("rand")
    assert book_list[0].title == "rand"

def test_borrow_books_by_query(b_cart):
    new_book = Book("Dune", "Jorge Trueba", "Fiction", 25.99)
    b_cart.retrieve_books(new_book)
    b_cart.borrow_books_by_query("Dune")
    data = b_cart.get_all_books()
    assert "Books" in data  
    assert all(book.get("title") != "Dune" for book in data["Books"].values())


