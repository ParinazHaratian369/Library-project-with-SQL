import customtkinter as ctk
from database import Database
from models import Book, BookStore
from tkinter import messagebox
class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bookstore Management")
        self.root.geometry("400x500")

        # database connection
        self.db = Database()
        self.bookstore = BookStore(self.db) 

        # GUI elements
        self.title_label = ctk.CTkLabel(root, text="Title")
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = ctk.CTkEntry(root)
        self.title_entry.grid(row=0, column=1)

        self.author_label = ctk.CTkLabel(root, text="Author")
        self.author_label.grid(row=1, column=0, padx=10, pady=10)
        self.author_entry = ctk.CTkEntry(root)
        self.author_entry.grid(row=1, column=1)

        self.genre_label = ctk.CTkLabel(root, text="Genre")
        self.genre_label.grid(row=2, column=0, padx=10, pady=10)
        self.genre_entry = ctk.CTkEntry(root)
        self.genre_entry.grid(row=2, column=1)

        self.price_label = ctk.CTkLabel(root, text="Price")
        self.price_label.grid(row=3, column=0, padx=10, pady=10)
        self.price_entry = ctk.CTkEntry(root)
        self.price_entry.grid(row=3, column=1)

        self.quantity_label = ctk.CTkLabel(root, text="Quantity")
        self.quantity_label.grid(row=4, column=0, padx=10, pady=10)
        self.quantity_entry = ctk.CTkEntry(root)
        self.quantity_entry.grid(row=4, column=1)

        self.add_button = ctk.CTkButton(root, text="Add Book", command=self.add_book)
        self.add_button.grid(row=5, column=1, pady=10)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()

        if not title or not author or not genre or not price or not quantity:
            messagebox.showerror("Input Error", "All fiels must be filled out")
            return
        
        try:
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Input Error", "Price and Quantity must be valid numbers")
            return
        

if __name__ == "__main__":
    root = ctk.CTk()
    app = BookstoreApp(root)
    root.mainloop()