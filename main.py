from library_system.book import Fiction
from library_system.library import Library

def main():
    lib=Library("City Library")
    book1=Fiction("The Hobbit", "J.R.R. Tolkien", "Fantasy")
    book2 = Fiction("Pride and Prejudice", "Jane Austen", "Romance")

    lib.add_books(book1)
    lib.add_books(book2)

    print(lib.display_books())

if __name__ == "__main__":
    main()