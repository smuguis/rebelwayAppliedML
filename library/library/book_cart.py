


import json
from dataclasses import dataclass, field
from library.books import Book
from library.random_number_utils import RandomUtils
from library.file_io import Fstream

@dataclass
class Books_Cart:
    database_path: str
    isEmpty: bool = True
    isActive: bool = False
    id: str = field(init=False, default_factory=RandomUtils.generate_random_id)

    def get_all_books(self, verbose=0)->dict:
        """
        reads and return hash map with all available books

        Args:
            if verbose is set to 1, it will print all the books.

            Returns:
            dict: a hash map with all the books in the database.

        """

        data_file = Fstream.load_json_file(self.database_path)

        if len(data_file.items())>0:
            self.isEmpty = False
            self.isActive = True

        try:
            if verbose == 1:
                Fstream.print_json_structure(data_file)
                return data_file
            else:
                return data_file
            
        except:
            raise ValueError("The value for he verbose as to be 0 or 1")
        

    def search_books(self, query: str)->list[Book]:
        """"""
        data = Fstream.load_json_file(self.database_path)
        matching_items = []
        for book_id, book_data in data["Books"].items():
            book = Book(title = book_data["title"], author = book_data["author"], genre = book_data["genre"], _price = book_data["price"], id = book_id)
            if query.lower() in book.search_string.lower():
                matching_items.append(book)

        if len(matching_items)==0:
            print("Not books found")

        else:
            for book in matching_items:
                print(f"Found: {book.title} {book.author} {book.genre} ${book._price}")

        return matching_items

    def borrow_books_by_query(self, query:str):
        """
        remove book by name from user
        """
        data = Fstream.load_json_file(self.database_path)
        books_to_remove = []

        for books_id, books_data in data["Books"].items():
            if query.lower() in books_data["title"].lower():
                books_to_remove.append(books_id)

        if not books_to_remove:
            print(f"no books mathing '{query}'")
            return

        for books_id in books_to_remove:
            book_name = data["Books"][books_id]["title"]
            del data["Books"][books_id]
            print(f"Book '{book_name}' has been borrowed from the library")
        with open(self.database_path, "w") as file:
            json.dump(data, file, indent=4)
        if not data["Books"]:
            self.isEmpty = True
            self.isActive = False

    def retrieve_books(self, book:Book):
        """
        retrieve book from user
        """
        data = self.get_all_books()

        new_book = {
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "price": book._price,
            "id": book.id
        }

        data["Books"][book.id] = new_book
        with open(self.database_path, "w") as file:
            json.dump(data, file, indent=4)
        self.isEmpty = False
        self.isActive = True

        print(f"Book '{book.title}' has been retrieved to the library")

    def empty_book_cart(self):
        """
        empty book cart
        """
        data = self.get_all_books()
        if len(data["Books"]) > 0:
            data = {"Books":{}}
            with open(self.database_path, "w") as file:
                json.dump(data, file, indent=4)
            
            if not data["Books"]:
                self.isEmpty = True
                self.isActive = False

        print("Book cart is empty")

        
                                        


