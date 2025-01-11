class Book:
    """Base class for books."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class for electronic books."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class for printed books."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class to represent a library that manages a collection of books."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a book (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Only instances of Book or its subclasses can be added to the library.")

    def list_books(self):
        """Prints details of all books in the library."""
        for book in self.books:
            print(book)
