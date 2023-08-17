import tkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


root = tk.Tk()
root.title("Calculator Project")

entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9",
    "4", "5", "6",
    "1", "2", "3",
    "0"
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: button_click(b)).grid(row=row_val,
                                                                                                  column=col_val)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

operators = [
    ("+", 1, 3),
    ("-", 2, 3),
    ("*", 3, 3),
    ("/", 4, 3),
    ("=", 4, 0),
    ("C", 4, 2)
]

for (operator, row, col) in operators:
    if operator == "C":
        tk.Button(root, text=operator, padx=20, pady=20, command=clear).grid(row=row, column=col)
    else:
        tk.Button(root, text=operator, padx=20, pady=20,
                  command=lambda o=operator: button_click(o) if o != "=" else calculate()).grid(row=row, column=col)

root.mainloop()
