import tkinter as tk
from tkinter import filedialog, messagebox
import os

class MenuExtractorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Extractor GUI")

        self.text_area = tk.Text(root, wrap=tk.WORD, width=50, height=20)
        self.text_area.pack(pady=10)

        self.load_button = tk.Button(root, text="Load Menu Items", command=self.load_menu_items)
        self.load_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Menu Items", command=self.save_menu_items)
        self.save_button.pack(pady=5)

    def load_menu_items(self):
        try:
            with open("menu_items.txt", "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
        except FileNotFoundError:
            messagebox.showerror("Error", "menu_items.txt not found")

    def save_menu_items(self):
        content = self.text_area.get(1.0, tk.END)
        with open("menu_items.txt", "w") as file:
            file.write(content)
        messagebox.showinfo("Success", "Menu items saved successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuExtractorGUI(root)
    root.mainloop()
