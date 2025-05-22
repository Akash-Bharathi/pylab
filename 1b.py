class Book: 
    def __init__(self, title, author): 
        self.title = title 
        self.author = author 
        self.is_borrowed = False 
class Member: 
    def __init__(self, name): 
        self.name = name 
        self.borrowed_books = [] 
    def borrow_book(self, book): 
        if not book.is_borrowed: 
            book.is_borrowed = True 
            self.borrowed_books.append(book) 
            print(f"{self.name} borrowed '{book.title}'.") 
        else: 
            print(f"'{book.title}' is already borrowed.") 
    def return_book(self, book): 
        if book in self.borrowed_books: 
            book.is_borrowed = False 
            self.borrowed_books.remove(book) 
            print(f"{self.name} returned '{book.title}'.") 
        else: 
            print(f"{self.name} didn't borrow '{book.title}'.") 
class Library: 
    def __init__(self): 
        self.books = [] 
    def add_book(self, book): 
        self.books.append(book) 
    def display_available_books(self): 
        print("Available books:") 
        for book in self.books: 
            if not book.is_borrowed: 
                print(f"- {book.title} by {book.author}") 
# Example usage with user input: 
library = Library() 
library.add_book(Book("1984", "George Orwell")) 
library.add_book(Book("To Kill a Mockingbird", "Harper Lee")) 
member_name = input("Enter member name: ") 
member = Member(member_name) 
library.display_available_books() 
book_title = input("Enter the title of the book to borrow: ") 
book_to_borrow = next((b for b in library.books if b.title == book_title), None) 
if book_to_borrow: 
    member.borrow_book(book_to_borrow) 
    library.display_available_books() 
# To return a book: 
return_title = input("Enter the title of the book to return: ") 
book_to_return = next((b for b in member.borrowed_books if b.title == 
return_title), None) 
if book_to_return: 
    member.return_book(book_to_return) 
    library.display_available_books()