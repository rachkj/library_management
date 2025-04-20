from abc import ABC,abstractmethod

class Book(ABC):
    def __init__(self, title, author):
        self._title=title
        self._author=author

    @abstractmethod
    def get_details(self):
        return f"{self._title} book has author {self._author}"
    
    def get_title(self):
        return self._title
    
class Fiction(Book):
    def __init__(self, title, author, genre):
        super().__init__(title,author)
        self._genre=genre

    def get_details(self):
        return f"{super().get_details()}, and genre is {self._genre}"
    

