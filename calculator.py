import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.configure(bg="#F0F0F0")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(self.root, textvariable=self.result_var, font=("Helvetica", 16), bd=10, relief=tk.GROOVE, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Helvetica", 14), bg="#D3D3D3", padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")
            self.root.grid_columnconfigure(col, weight=1)
            self.root.grid_rowconfigure(row, weight=1)

    def on_button_click(self, value):
        if value == 'C':
            self.result_var.set("")
        elif value == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.result_var.set("")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + value)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
