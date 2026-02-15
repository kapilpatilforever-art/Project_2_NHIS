import tkinter as tk
from tkinter import messagebox
import math

# Main Window
root = tk.Tk()
root.title("Smart Calculator - Kapil")
root.geometry("400x550")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

expression = ""
history_list = []

# Display Frame
display_frame = tk.Frame(root, bg="#1e1e1e")
display_frame.pack(pady=10)

display = tk.Entry(display_frame, font=("Arial", 22),
                   bg="#2d2d2d", fg="white",
                   bd=10, relief=tk.FLAT, justify="right")
display.pack(ipady=15, ipadx=10)

# History Box
history_box = tk.Text(root, height=5, bg="#252526",
                      fg="lightgreen", font=("Arial", 10))
history_box.pack(fill="both", padx=10, pady=5)


def update_display(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)


def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)


def backspace():
    global expression
    expression = expression[:-1]
    display.delete(0, tk.END)
    display.insert(tk.END, expression)


def calculate():
    global expression
    try:
        result = eval(expression)
        history_list.append(expression + " = " + str(result))
        history_box.insert(tk.END, expression + " = " + str(result) + "\n")
        expression = str(result)
        display.delete(0, tk.END)
        display.insert(tk.END, expression)
    except:
        messagebox.showerror("Error", "Invalid Expression")
        clear()


def square_root():
    global expression
    try:
        result = math.sqrt(float(expression))
        history_box.insert(tk.END, "√" + expression + " = " + str(result) + "\n")
        expression = str(result)
        display.delete(0, tk.END)
        display.insert(tk.END, expression)
    except:
        messagebox.showerror("Error", "Invalid Input")
        clear()


def square():
    global expression
    try:
        result = float(expression) ** 2
        history_box.insert(tk.END, expression + "² = " + str(result) + "\n")
        expression = str(result)
        display.delete(0, tk.END)
        display.insert(tk.END, expression)
    except:
        messagebox.showerror("Error", "Invalid Input")
        clear()


# Button Frame
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack()

buttons = [
    ('7', lambda: update_display('7')),
    ('8', lambda: update_display('8')),
    ('9', lambda: update_display('9')),
    ('/', lambda: update_display('/')),

    ('4', lambda: update_display('4')),
    ('5', lambda: update_display('5')),
    ('6', lambda: update_display('6')),
    ('*', lambda: update_display('*')),

    ('1', lambda: update_display('1')),
    ('2', lambda: update_display('2')),
    ('3', lambda: update_display('3')),
    ('-', lambda: update_display('-')),

    ('0', lambda: update_display('0')),
    ('.', lambda: update_display('.')),
    ('+', lambda: update_display('+')),
    ('=', calculate),

    ('C', clear),
    ('⌫', backspace),
    ('√', square_root),
    ('x²', square),
]

row = 0
col = 0

for (text, command) in buttons:
    button = tk.Button(button_frame,
                       text=text,
                       command=command,
                       width=7,
                       height=2,
                       font=("Arial", 14),
                       bg="#3c3c3c",
                       fg="white",
                       activebackground="#007acc",
                       activeforeground="white",
                       bd=0)
    button.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1


# Keyboard Support
def key_event(event):
    key = event.char
    if key in "0123456789+-*/.":
        update_display(key)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        backspace()

root.bind("<Key>", key_event)

root.mainloop()
