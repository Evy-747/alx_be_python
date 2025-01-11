class Book:
    """
    A class to represent a book with magic methods for construction, deletion, and string representation.
    """
    def __init__(self, title, author, year):
        """Initialize the book with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor method to handle cleanup when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for end-users."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation of the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

