from tkinter import *

def press(num):
    entry.insert(END, num)

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())  # Evaluates the mathematical expression
        entry.delete(0, END)
        entry.insert(END, str(result))
    except Exception as e:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Create GUI window
root = Tk()
root.title("Calculator")
root.geometry("300x400")

entry = Entry(root, width=16, font=("Arial", 20), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    Button(root, text=text, font=("Arial", 18), command=lambda t=text: press(t)).grid(row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5)

Button(root, text="C", font=("Arial", 18), command=clear).grid(row=5, column=0, columnspan=2, ipadx=35, ipady=10, pady=5)
Button(root, text="=", font=("Arial", 18), command=calculate).grid(row=5, column=2, columnspan=2, ipadx=35, ipady=10, pady=5)

root.mainloop()
