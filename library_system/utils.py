class Formatter:
    @staticmethod
    def format_book(book):
        return f"Book Info:\n  {book.get_details()}"