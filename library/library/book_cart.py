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

        if len(data_file.books())>0:
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

