from library.book_cart import Books_Cart
from library.books import Book

if __name__ == "__main__":
    database = "./database.json"
    my_books = Books_Cart(database)

    #search for an item
    print ("Searching Book...")
    results = my_books.search_books("la sombra")
    print("----------")
