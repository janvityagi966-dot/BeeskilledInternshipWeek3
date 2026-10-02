# Library Management System (OOP)
# Add/remove books, issue/return books

from datetime import date


class LibraryManagement:
    def __init__(self):
        self.books = {
            book_code: None
            for book_code in (1001, 1002, 1003, 1004, 2001, 2002, 2003, 2004)
        }

    @staticmethod
    def _get_book_code():
        while True:
            try:
                return int(input("Enter the book code: "))
            except ValueError:
                print("Please enter a valid book code.")

    def issue_books(self):
        name = input("Enter your Name: ")
        book_code = self._get_book_code()
        if book_code not in self.books:
            print("Book not found in the library.")
            return
        if self.books[book_code] is not None:
            print("Book is already issued.")
            return

        self.books[book_code] = name
        issue_date = date.today()
        print(f"Book issued to {name} on {issue_date}")

    def return_books(self):
        book_code = self._get_book_code()
        if book_code not in self.books:
            print("Book not found in the library.")
        elif self.books[book_code] is None:
            print("This book has not been issued.")
        else:
            self.books[book_code] = None
            print("Book returned successfully.")

    def add_books(self):
        book_code = self._get_book_code()
        if book_code in self.books:
            print("A book with that code already exists.")
        else:
            self.books[book_code] = None
            print("Book added successfully.")

    def remove_books(self):
        book_code = self._get_book_code()
        if book_code not in self.books:
            print("Book not found in the library.")
        elif self.books[book_code] is not None:
            print("Cannot remove a book while it is issued.")
        else:
            del self.books[book_code]
            print("Book removed successfully.")


def main():
    library = LibraryManagement()

    while True:
        print("\n1. Issue Books")
        print("2. Return Books")
        print("3. Add Books")
        print("4. Remove Books")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            library.issue_books()
        elif choice == "2":
            library.return_books()
        elif choice == "3":
            library.add_books()
        elif choice == "4":
            library.remove_books()
        elif choice == "5":
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
                        

        
