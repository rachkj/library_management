from library_system.utils import Formatter

class Library:
    def __init__(self, name):
        self._name=name
        self._books=[]

    def add_books(self,book):
        self._books.append(book)

    def display_books(self):
        if not self._books:
            return f"{self._name} has no books."
        output = f"{self._name} Books:\n"
        for book in self._books:
            # Importing and using function from another class
            output += Formatter.format_book(book) + "\n"
        return output