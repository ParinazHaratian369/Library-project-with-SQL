import customtkinter as ctk
class BookstoreApp:
    def __init__(self, root):
        self.root = root

if __name__ == "__main__":
    root = ctk.CTk()
    app = BookstoreApp(root)
    root.mainloop()