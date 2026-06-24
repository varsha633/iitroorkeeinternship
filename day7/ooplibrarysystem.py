class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"{self.title} by {self.author} ({status})"


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_issued:
            book.is_issued = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already issued")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_issued = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print("Book not borrowed by this member")

    def show_books(self):
        print(f"\nBooks borrowed by {self.name}:")
        for book in self.borrowed_books:
            print("-", book.title)

