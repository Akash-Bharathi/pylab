#3(B) Create a graphical calendar application with buttons to navigate
#through months and years, and display selected dates and events.

import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calendar")

        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

        # Header Frame for navigation
        header = ttk.Frame(root)
        header.pack()

        self.prev_btn = ttk.Button(header, text="<<", command=self.prev_month)
        self.prev_btn.grid(row=0, column=0)

        self.month_year_lbl = ttk.Label(header, text="", width=15, anchor='center')
        self.month_year_lbl.grid(row=0, column=1)

        self.next_btn = ttk.Button(header, text=">>", command=self.next_month)
        self.next_btn.grid(row=0, column=2)

        # Calendar Frame
        self.calendar_frame = ttk.Frame(root)
        self.calendar_frame.pack()

        # Label to show selected date
        self.date_lbl = ttk.Label(root, text="Select a date")
        self.date_lbl.pack(pady=10)

        self.show_calendar()

    def show_calendar(self):
        # Clear previous widgets
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        # Update header label
        self.month_year_lbl.config(
            text=f"{calendar.month_name[self.current_month]} {self.current_year}"
        )

        # Weekday headers
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for idx, day in enumerate(days):
            ttk.Label(self.calendar_frame, text=day).grid(row=0, column=idx)

        # Get calendar matrix
        cal = calendar.Calendar(firstweekday=0).monthdayscalendar(
            self.current_year, self.current_month
        )

        # Create buttons for days
        for row_idx, week in enumerate(cal, start=1):
            for col_idx, day in enumerate(week):
                if day == 0:
                    continue
                btn = ttk.Button(
                    self.calendar_frame,
                    text=str(day),
                    command=lambda d=day: self.select_date(d)
                )
                btn.grid(row=row_idx, column=col_idx, padx=2, pady=2)

    def select_date(self, day):
        self.date_lbl.config(
            text=f"Selected Date: {day}-{self.current_month}-{self.current_year}"
        )

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.show_calendar()

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.show_calendar()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()

    if __name__ == "__main__": 
        root = tk.Tk() 
        app = CalendarApp(root) 
        root.mainloop()
