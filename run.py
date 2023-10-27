# run.py

import tkinter as tk
from tkinter import simpledialog, messagebox

try:
    from src.main import PasswordManagerApp

    def get_app_password():
        try:
            password = simpledialog.askstring("Password", "Enter the application password:", show="*")
            return password
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            return None

    if __name__ == "__main__":
        try:
            # Ask for the application password
            app_password = get_app_password()

            if app_password == "APP_PASSWORD":  # Replace with your chosen app password
                root = tk.Tk()
                app = PasswordManagerApp(root)
                root.mainloop()
            elif app_password is not None:
                messagebox.showerror("Error", "Incorrect application password. Please try again.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
except Exception as e:
    messagebox.showerror("Error", f"An error occurred: {e}")
