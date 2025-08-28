class Book:
    def __init__(self, title, author, genre):
        self.book_title = title
        self.book_author = author
        self.book_genre = genre
        self.is_available = True
    
    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Book {self.book_title} has been borrowed!")
        else:
            print("Book is not available")
    
    def return_book(self):
        self.is_available = True
        print(f"Book {self.book_title} has been returned!")

book_1 = Book("Python 101", "John Snow", "Coding")
book_2 = Book("Linux Basics for Hackers", "OTW", "Linux & Hacking")

book_1.borrow()
book_1.return_book()

book_2.borrow()
book_2.return_book()



