from library.books import Book

def test_book_price()->None:
    new_book = Book("dummy","Marie", "Mistery", 50.02)
    assert new_book.price >= 0.0 or new_book.price == 50.02

def test_book_title()->None:
    new_book_02 = Book("rutu", "b", "c", 16.00)
    assert len(new_book_02.title) > 0
