import customtkinter as ctk
class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title = "Bookstore Management"
        self.root.geometry = "300x400"

if __name__ == "__main__":
    root = ctk.CTk()
    app = BookstoreApp(root)
    root.mainloop()