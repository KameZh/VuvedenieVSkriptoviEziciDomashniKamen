import os
class LibraryAccount:
    name = ""
    borrowed_books = []
    number_of_books = 0
    def borrow_book(self, book_name):
        if self.number_of_books >= 3:
            print(f"{self.name} cannot borrow more than 3 books.")
            return
        else:
            if book_name in self.borrowed_books:
                print(f"{self.name} has already borrowed '{book_name}'.")
            else:
                self.borrowed_books.append(book_name)
                print(f"{self.name} borrowed '{book_name}'.")
                self.number_of_books += 1
    def return_book(self, book_name):
        if book_name == "all":
            self.borrowed_books.clear()
            self.number_of_books = 0
            print(f"{self.name} returned all books.")
            return
        if book_name in self.borrowed_books:
            self.borrowed_books.remove(book_name)
            print(f"{self.name} returned '{book_name}'.")
            self.number_of_books -= 1
        else:
            print(f"{self.name} does not have '{book_name}' borrowed.")
    def list_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"{self.name} has borrowed the following books ({self.number_of_books}):")
            for book in self.borrowed_books:
                print(f"- {book}")

account = LibraryAccount()
account.name = input("Enter your name: ")
while True:
    os.system('cls')
    print(f"Welcome, {account.name}!")
    print(f"You can borrow up to 3 books. {account.number_of_books} books currently borrowed.")
    print("===================================")
    action = input("Would you like to borrow(b), return(r), list books(l), or exit(ext)? ").lower()
    if action == "borrow" or action == "b":
        os.system('cls')
        book_name = input("Enter the name of the book to borrow: ")
        account.borrow_book(book_name)
        input("Press any key to continue...")
    elif action == "return" or action == "r":
        os.system('cls')
        print("Current borrowed books:")
        account.list_books()
        print("===================================")
        book_name = input("Enter the name of the book to return (enter 'all' to return all): ")
        account.return_book(book_name)
        input("Press any key to continue...")
    elif action == "list books" or action == "l":
        os.system('cls')
        account.list_books()
        input("Press and key to continue...")
    elif action == "exit" or action == "ext":
        os.system('cls')
        print("Exiting the library account system.")
        break
    else:
        print("Invalid action. Please choose borrow, return, list books, or exit.")