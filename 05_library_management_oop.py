# A small library system demonstrating classes and object interaction.

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def display(self):
        status = "Available" if self.copies > 0 else "Out of stock"
        print(f"{self.title} by {self.author} | Copies: {self.copies} | {status}")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title):
        book = self.find_book(title)
        if book is None:
            print("Book not found.")
        elif book.copies == 0:
            print("No copies are currently available.")
        else:
            book.copies -= 1
            print(f"You borrowed '{book.title}'.")

    def return_book(self, title):
        book = self.find_book(title)
        if book is None:
            print("This library does not have that title.")
        else:
            book.copies += 1
            print(f"'{book.title}' has been returned.")

    def show_catalogue(self):
        print(f"\\nCatalogue: {self.name}")
        print("=" * 45)
        for book in self.books:
            book.display()


def main():
    library = Library("Campus Library")
    library.add_book(Book("Python Basics", "A. Sharma", 3))
    library.add_book(Book("Learning OOP", "R. Verma", 2))
    library.add_book(Book("Data Science Intro", "N. Rao", 1))

    library.show_catalogue()
    library.borrow_book("Python Basics")
    library.borrow_book("Data Science Intro")
    library.borrow_book("Data Science Intro")
    library.return_book("Data Science Intro")
    library.show_catalogue()


if __name__ == "__main__":
    main()
