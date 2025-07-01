import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("300x400")
root.configure(bg="#1e1e2f")  # Dark background

# Expression variable
expression = ""

# Update the expression when a button is pressed
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Evaluate the expression
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

# Clear the entry
def clear():
    global expression
    expression = ""
    equation.set("")

# String variable to hold current expression
equation = tk.StringVar()

# Entry field to show input/output
entry = tk.Entry(root, textvariable=equation, font=('Arial', 20),
                 bd=10, insertwidth=2, width=14, borderwidth=4, justify='right',
                 bg="#2d2d44", fg="white")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, pady=5)

# Helper function to create colored buttons
def create_btn(text, row, col, cmd, bg="#3b3b5c", fg="white", colspan=1):
    tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
              bg=bg, fg=fg, activebackground="#5c5c8a",
              command=cmd).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

# Row 1 (7 8 9 /)
create_btn('7', 1, 0, lambda: press(7))
create_btn('8', 1, 1, lambda: press(8))
create_btn('9', 1, 2, lambda: press(9))
create_btn('/', 1, 3, lambda: press('/'), bg="#ff5e5e")

# Row 2 (4 5 6 *)
create_btn('4', 2, 0, lambda: press(4))
create_btn('5', 2, 1, lambda: press(5))
create_btn('6', 2, 2, lambda: press(6))
create_btn('*', 2, 3, lambda: press('*'), bg="#ff5e5e")

# Row 3 (1 2 3 -)
create_btn('1', 3, 0, lambda: press(1))
create_btn('2', 3, 1, lambda: press(2))
create_btn('3', 3, 2, lambda: press(3))
create_btn('-', 3, 3, lambda: press('-'), bg="#ff5e5e")

# Row 4 (0 . = +)
create_btn('0', 4, 0, lambda: press(0))
create_btn('.', 4, 1, lambda: press('.'))
create_btn('=', 4, 2, equalpress, bg="#4caf50")  # green
create_btn('+', 4, 3, lambda: press('+'), bg="#ff5e5e")

# Row 5 (Clear button across all columns)
create_btn('C', 5, 0, clear, bg="#607d8b", colspan=4)

# Make the grid expandable
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

# Start the GUI loop
root.mainloop()
