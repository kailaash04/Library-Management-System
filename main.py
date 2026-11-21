
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.availability = True

    def __str__(self):
        status = "Available" if self.availability else "Borrowed"
        return f"{self.name} by {self.author} [{status}]"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def borrow(self, name):
        for book in self.books:
            if book.name == name:
                if book.availability:
                    book.availability = False
                    print("Book borrowed successfully!")
                else:
                    print("Book is already borrowed!")
                return

        print("Book not found!")

    def return_book(self, name):
        for book in self.books:
            if book.name == name:
                if not book.availability:
                    book.availability = True
                    print("Book returned successfully!")
                else:
                    print("Book was not borrowed!")
                return

        print("Book not found!")

    def show_books(self):
        if not self.books:
            print("Library is empty!")
            return

        for book in self.books:
            print(book)


# Creating a Library object
library = Library()

# Creating Book objects
book1 = Book("Python 101", "Rao")
book2 = Book("Java Basics", "Kumar")
book3 = Book("SQL Fundamentals", "Vijay")

# Adding books
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Displaying books
print("\n--- Library Books ---")
library.show_books()

# Borrowing a book
print("\n--- Borrowing Book ---")
library.borrow("Python 101")

# Displaying updated availability
print("\n--- Updated Library ---")
library.show_books()

# Returning a book
print("\n--- Returning Book ---")
library.return_book("Python 101")

# Displaying final availability
print("\n--- Final Library ---")
library.show_books()
