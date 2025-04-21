class Book:
    def __init__(self, title, author, genre, price, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.quantity = quantity

class BookStore:
    def __init__(self, db):
        self.db = db

    def add_book(self, book):
        query = "INSERT INTO book (title, author, genre, price, quantity) VALUES (%s, %s, %s, %s, %s)"
        params = (book.title, book.author, book.genre, book.price, book.quantity)
        