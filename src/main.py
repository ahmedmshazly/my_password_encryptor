# main.py

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog
from src.encryptor import encrypt, decrypt
from src.file_manager import write_to_file, read_from_file

class PasswordManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.geometry("600x400")

        self.notebook = ttk.Notebook(master)

        # Tab 1: Encrypt Password
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Encrypt Password")
        self.setup_encrypt_tab()

        # Tab 2: Decrypt Password
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Decrypt Password")
        self.setup_decrypt_tab()

        # Tab 3: View Stored Passwords
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="View Stored Passwords")
        self.setup_view_tab()

        self.notebook.pack(expand=True, fill="both")

    def setup_encrypt_tab(self):
        ttk.Label(self.tab1, text="Website Name (first capital all lower):").pack(pady=10)  # Changed from "Website URL"
        self.name_entry = ttk.Entry(self.tab1, width=40)  # Changed from "self.name_entry"
        self.name_entry.pack(pady=5)  # Changed from "self.name_entry"

        ttk.Label(self.tab1, text="Keyword (first capital all lower):").pack(pady=10)
        self.keyword_entry = ttk.Entry(self.tab1, show="*", width=40)
        self.keyword_entry.pack(pady=5)

        ttk.Button(self.tab1, text="Encrypt Password", command=self.encrypt_password).pack(pady=10)

    def encrypt_password(self):
        website_url = self.name_entry.get()
        keyword = self.keyword_entry.get()

        try:
            encrypted_password = encrypt(website_url, keyword)
            self.show_message("Password Encrypted Successfully!")
            self.copy_to_clipboard(encrypted_password)
            write_to_file(encrypted_password)
        except ValueError as e:
            self.show_error(str(e))

    def setup_decrypt_tab(self):
        ttk.Label(self.tab2, text="Encrypted Password:").pack(pady=10)
        self.encrypted_password_entry = ttk.Entry(self.tab2, show="*", width=40)
        self.encrypted_password_entry.pack(pady=5)

        ttk.Label(self.tab2, text="Keyword:").pack(pady=10)
        self.decrypt_keyword_entry = ttk.Entry(self.tab2, show="*", width=40)
        self.decrypt_keyword_entry.pack(pady=5)

        ttk.Button(self.tab2, text="Decrypt Password", command=self.decrypt_password).pack(pady=10)

    def decrypt_password(self):
        encrypted_password = self.encrypted_password_entry.get()
        keyword = self.decrypt_keyword_entry.get()

        try:
            decrypted_password = decrypt(encrypted_password, keyword)
            self.show_message("Password Decrypted Successfully!")
            self.copy_to_clipboard(decrypted_password)
        except Exception as e:
            self.show_error(str(e))

    def setup_view_tab(self):
        self.passwords_listbox = tk.Listbox(self.tab3, width=50)
        self.passwords_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        # Add a vertical scrollbar to the listbox
        scrollbar = tk.Scrollbar(self.tab3, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the listbox to use the scrollbar
        self.passwords_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.passwords_listbox.yview)

        self.load_stored_passwords()

        ttk.Button(self.tab3, text="Show Password", command=self.show_selected_password).pack(pady=10)

    def load_stored_passwords(self):
        passwords = read_from_file()
        for password in passwords:
            self.passwords_listbox.insert(tk.END, "*" * len(password))

    def show_selected_password(self):
        selected_index = self.passwords_listbox.curselection()
        if selected_index:
            selected_password = read_from_file()[selected_index[0]]
            main_app_password = self.get_app_password()  # Get the main app password

            if main_app_password == "APP_PASSWORD2":  # Replace with your chosen app password
                self.show_message("Password Accessed Successfully!")
                self.copy_to_clipboard(selected_password)
            else:
                self.show_error("Incorrect application password. Please try again.")




    def get_app_password(self):
        password = simpledialog.askstring("Password", "Enter the application password:", show="*")
        return password

    def copy_to_clipboard(self, text):
        self.master.clipboard_clear()
        self.master.clipboard_append(text)
        self.master.update()

    def show_message(self, message):
        messagebox.showinfo("Message", message)

    def show_error(self, error_message):
        messagebox.showerror("Error", error_message)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
