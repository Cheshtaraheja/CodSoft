import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def update_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        updated_task = task_entry.get()
        if updated_task:
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task!")
    else:
        messagebox.showwarning("Warning", "Please select a task to update!")

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("To-Do List- CHESHTA")

# Task Entry and Add Button
task_entry = tk.Entry(app, width=50)
task_entry.pack(pady=10)
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()

# Listbox to display tasks
tasks_listbox = tk.Listbox(app, width=50)
tasks_listbox.pack(pady=5)

# Remove, Update, and Clear Buttons
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=5)
update_button = tk.Button(app, text="Update Task", command=update_task)
update_button.pack(side=tk.LEFT, padx=5)
clear_button = tk.Button(app, text="Clear All", command=clear_tasks)
clear_button.pack(side=tk.LEFT, padx=5)

# Start the main event loop
app.mainloop()
