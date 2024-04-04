class Book:
    def __init__(self, title, author, code):
        self.title = title
        self.author = author
        self.code = code
        self.status = True
    
    def check_out(self):
        if self.status:
            self.status = False
            return True
        else:
            return False
    
    def return_book(self):
        if not self.status:
            self.status = True
            return True
        else:
            return False

class Library:
    def __init__(self):
        self.books_list = []
        
    def add_book(self, book):
        self.books_list.append(book)
    
    def search_book(self, word_to_search):
        found_book = False
        for book in self.books_list:
            if word_to_search in [book.author, book.title] and book.status:
                print(f"Title: {book.title}, Author: {book.author}, Code: {book.code}")
                found_book = True    
        if not found_book:
            print("There is no book regarding the searched word")                         
    
    def display_books(self):
        for book in self.books_list:
            print(f"Title: {book.title}, Author: {book.author}, Code: {book.code}")

class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.user_books_list = []
    
    def check_out(self, library, word_to_search):
        for book in library.books_list:
            if word_to_search in [book.author, book.title] and book.status:
                print(f"The book '{book.title}' is available and now you can take it")
                if book.check_out():
                    self.user_books_list.append(book)
                    return
        print("There is no book available with that name or author") 
    
    def return_book(self, library, code):
        for book in self.user_books_list:
            if code == book.code:
                if book.return_book():
                    library.add_book(book)
                    self.user_books_list.remove(book)
                    print(f"The book '{book.title}' has been returned successfully")
                    return
        print("You don't have any book with that code") 

# Ejemplo de uso
library = Library()
book1 = Book("Python Basics", "John Smith", "PY101")
book2 = Book("Machine Learning", "Alice Johnson", "ML202")
library.add_book(book1)
library.add_book(book2)

user = User("Alice")
user.check_out(library, "Machine Learning")

print("\nBooks currently in the library:")
library.display_books()

print("\nBooks currently with the user:")
for book in user.user_books_list:
    print(f"Title: {book.title}, Author: {book.author}, Code: {book.code}")

print("\nReturning a book...")
user.return_book(library, "ML202")

print("\nBooks currently in the library after return:")
library.display_books()

 










