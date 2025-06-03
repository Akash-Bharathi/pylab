#3(A) Create a graphical calculator with buttons for numeric inputs,
#arithmetic operations and show the results
import tkinter as tk

def on_button_click(char):
    if char == 'C':
        input_field.delete(0, tk.END)
    elif char == '=':
        try:
            result = eval(input_field.get())
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, str(result))
        except Exception:
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, "Error")
    else:
        input_field.insert(tk.END, char)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the input field
input_field = tk.Entry(root, width=30, justify="right", font=("Arial", 14))
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place buttons
row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 12),
              command=lambda char=button: on_button_click(char)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the GUI event loop
root.mainloop()
