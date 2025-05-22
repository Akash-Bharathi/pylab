#4(b) Develop a GUI-based notes application where users can create, edit, and manage notes with features like formatting text, saving notes, and organizing them into categories.

import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

class NotesApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Notes App")

        self.categories = {}
        self.current_category = None
        self.current_note = None

        # Category frame
        cat_frame = ttk.Frame(master)
        cat_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        ttk.Label(cat_frame, text="Categories").pack()
        self.cat_listbox = tk.Listbox(cat_frame)
        self.cat_listbox.pack(fill=tk.Y, expand=True)
        self.cat_listbox.bind('<<ListboxSelect>>', self.load_notes)
        ttk.Button(cat_frame, text="Add Category", command=self.add_category).pack(pady=5)

        # Notes list frame
        note_frame = ttk.Frame(master)
        note_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        ttk.Label(note_frame, text="Notes").pack()
        self.note_listbox = tk.Listbox(note_frame)
        self.note_listbox.pack(fill=tk.Y, expand=True)
        self.note_listbox.bind('<<ListboxSelect>>', self.load_note)
        ttk.Button(note_frame, text="Add Note", command=self.add_note).pack(pady=5)

        # Editor frame
        editor_frame = ttk.Frame(master)
        editor_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.text_area = tk.Text(editor_frame, wrap='word')
        self.text_area.pack(fill=tk.BOTH, expand=True)
        ttk.Button(editor_frame, text="Save Note", command=self.save_note).pack(pady=5)

    def add_category(self):
        name = simpledialog.askstring("New Category", "Category name:")
        if name and name not in self.categories:
            self.categories[name] = {}
            self.cat_listbox.insert(tk.END, name)

    def load_notes(self, event=None):
        selection = self.cat_listbox.curselection()
        if selection:
            index = selection[0]
            category = self.cat_listbox.get(index)
            self.current_category = category
            self.note_listbox.delete(0, tk.END)
            for note in self.categories[category]:
                self.note_listbox.insert(tk.END, note)

    def add_note(self):
        if self.current_category:
            title = simpledialog.askstring("New Note", "Note title:")
            if title and title not in self.categories[self.current_category]:
                self.categories[self.current_category][title] = ""
                self.note_listbox.insert(tk.END, title)
                self.current_note = title
                self.text_area.delete('1.0', tk.END)

    def load_note(self, event=None):
        selection = self.note_listbox.curselection()
        if selection:
            index = selection[0]
            title = self.note_listbox.get(index)
            self.current_note = title
            content = self.categories[self.current_category][title]
            self.text_area.delete('1.0', tk.END)
            self.text_area.insert(tk.END, content)

    def save_note(self):
        if self.current_category and self.current_note:
            content = self.text_area.get('1.0', tk.END)
            self.categories[self.current_category][self.current_note] = content
            messagebox.showinfo("Saved", "Note saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()
