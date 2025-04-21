import customtkinter as ctk
from database import Database
from models import Book, BookStore
class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bookstore Management")
        self.root.geometry("400x500")

        # database connection
        self.db = Database()        

if __name__ == "__main__":
    root = ctk.CTk()
    app = BookstoreApp(root)
    root.mainloop()