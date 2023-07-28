import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    password_length = length_entry.get()

    if not password_length.isdigit():
        messagebox.showerror("Error", "Please enter a valid number for password length.")
        return

    password_length = int(password_length)
    
    if password_length < 6:
        messagebox.showerror("Error", "Password length should be at least 6 characters.")
        return

    complexity = complexity_var.get()
    characters = ''

    if complexity == 1:  # Simple
        characters = string.ascii_letters
    elif complexity == 2:  # Moderate
        characters = string.ascii_letters + string.digits
    elif complexity == 3:  # Complex
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Password length input
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=10)
length_entry = tk.Entry(root, width=20)
length_entry.pack(pady=5)

# Complexity selection
complexity_label = tk.Label(root, text="Select Complexity:")
complexity_label.pack(pady=10)
complexity_var = tk.IntVar()
simple_radio = tk.Radiobutton(root, text="Simple", variable=complexity_var, value=1)
simple_radio.pack()
moderate_radio = tk.Radiobutton(root, text="Moderate", variable=complexity_var, value=2)
moderate_radio.pack()
complex_radio = tk.Radiobutton(root, text="Complex", variable=complexity_var, value=3)
complex_radio.pack()

# Generate password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password,bg="lightblue",fg="black", activebackground="teal")
generate_button.pack(pady=20)

# Password display label
password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()
