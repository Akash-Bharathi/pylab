#4(a) Develop a GUI based to do list application where user can
#add, delete and manage their task


import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)  # Clear the entry after adding

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_task_list()

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Main window setup
root = tk.Tk()
root.title("To-Do List")

tasks = []

# Task entry
task_entry = tk.Entry(root, width=30)
task_entry.grid(row=0, column=0, padx=5, pady=5)

# Add and Delete buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=2, padx=5, pady=5)

# Task display listbox
task_listbox = tk.Listbox(root, width=50)
task_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Initialize task list
update_task_list()

# Start the GUI event loop
root.mainloop()
