from abc import ABC, abstractmethod

# ————————— Person Base Class —————————
class Person():
    def __init__(self, name, email):
        self.name =name
        self.email = email
   
    def get_info(self):
        print(f"Name: {self.name}, Email: {self.email}")    
        
# ————————— Member Class —————————     

class Member(Person):
    def __init__ (self, name, email, memeber_id):
        super().__init__(name, email)
        self.member_id = memeber_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            return f"Book '{book.title}' borrowed successfully."
        else:
            return f"Book '{book.title}' is not available."
        
# ————————— Librarian Class —————————
class Librarian(Person):
    def __init__ (self, name, email, employee_id, salary):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.salary = salary
        self. books = []
        
    def add_book(self, book):
        self.books.append(book)
        return f"Book '{book.title}' added successfully." 
                
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return f"Book '{book.title}' removed successfully."
        else:
            return f"Book '{book.title}' not found in the library."            
    
# ————————— Book Class —————————

class Book():
    def __init__ (self, title, author, isbn, available=True):   
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        
    def get_book_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}")
        #return self.title, self.author, self.isbn, self.available    
        
# ————————— Library Class —————————

class Library():
    def __init__ (self, name):
     self.name = name
     self.books = []
     self.members = []
    
    def add_member(self, member):
        self.members.append(member)
        return f"Member '{member.name}' added successfully."
    
    def list_available_books(self):
        return [book.get_book_info() for book in self.books if book.available]
    
# Create library
lib = Library("City Library")

# Create librarian
librarian = Librarian("Alice", "alice@gmail.com", 101, 50000)

# Create members
member1 = Member("Bob", "bob@gmail.com", 201)
member2 = Member("Tayyab", "tayyab@gmail.com", 202)

# Add members to library
print(lib.add_member(member1))
print(lib.add_member(member2))

# Create books
book1 = Book("Python Programming", "Guido van Rossum", "ISBN-123")
book2 = Book("Data Science", "Andrew Ng", "ISBN-456")
book3 = Book("Machine Learning", "Tom Mitchell", "ISBN-789")

# Add books to library via librarian
print(librarian.add_book(book1))
print(librarian.add_book(book2))

# Member borrows a book
print(member1.borrow_book(book1))

# Member tries to borrow the same book again
print(member2.borrow_book(book1))

# Member returns a book
book1.available = True
print(f"Book '{book1.title}' returned successfully.")

# Now another member can borrow it
print(member2.borrow_book(book1))

# View available books
print("Available Books:")
for b in lib.list_available_books():
    print(b)
