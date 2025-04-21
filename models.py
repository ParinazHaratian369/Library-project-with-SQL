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
        pass