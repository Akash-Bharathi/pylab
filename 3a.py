import tkinter as tk 
def on_button_click(char): 
    if char == 'C': 
        input_field.delete(0, tk.END) 
    elif char == '=': 
        try: 
            result = eval(input_field.get()) 
            input_field.delete(0, tk.END) 
            input_field.insert(tk.END, str(result)) 
        except Exception as e: 
            input_field.delete(0, tk.END) 
            input_field.insert(tk.END, "Error") 
        else: 
            input_field.insert(tk.END, char) 
            root = tk.Tk() 
            root.title("Calculator") 
            input_field = tk.Entry(root, width=30, justify="right") 
            input_field.grid(row=0, column=0, columnspan=4) 

            buttons = [ 
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+' 
            ] 
            row = 1 
            col = 0 
            for button in buttons: 
                tk.Button(root, text=button, width=5, height=2, 
                command=lambda char=button: on_button_click(char)).grid(row=row, 
                column=col) 
                col += 1 
            if col > 3: 
                col = 0 
                row += 1 
root.mainloop()