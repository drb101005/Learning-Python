import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# This string holds the expression to be evaluated
expression = ""

# Function to update the expression in the entry widget
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    global expression
    try:
        total = str(eval(expression))  # Evaluate the expression using eval()
        equation.set(total)
        expression = total  # Allow further calculation with result
    except:
        equation.set("Error")
        expression = ""

# Function to clear the entry field
def clear():
    global expression
    expression = ""
    equation.set("")

# StringVar to update the entry widget dynamically
equation = tk.StringVar()

# Entry field to show the expression / result
entry = tk.Entry(root, textvariable=equation, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10)

# Buttons (7 to 9)
tk.Button(root, text='7', padx=20, pady=20, font=('Arial', 14), command=lambda: press(7)).grid(row=1, column=0)
tk.Button(root, text='8', padx=20, pady=20, font=('Arial', 14), command=lambda: press(8)).grid(row=1, column=1)
tk.Button(root, text='9', padx=20, pady=20, font=('Arial', 14), command=lambda: press(9)).grid(row=1, column=2)
tk.Button(root, text='/', padx=20, pady=20, font=('Arial', 14), command=lambda: press('/')).grid(row=1, column=3)

# Buttons (4 to 6)
tk.Button(root, text='4', padx=20, pady=20, font=('Arial', 14), command=lambda: press(4)).grid(row=2, column=0)
tk.Button(root, text='5', padx=20, pady=20, font=('Arial', 14), command=lambda: press(5)).grid(row=2, column=1)
tk.Button(root, text='6', padx=20, pady=20, font=('Arial', 14), command=lambda: press(6)).grid(row=2, column=2)
tk.Button(root, text='*', padx=20, pady=20, font=('Arial', 14), command=lambda: press('*')).grid(row=2, column=3)

# Buttons (1 to 3)
tk.Button(root, text='1', padx=20, pady=20, font=('Arial', 14), command=lambda: press(1)).grid(row=3, column=0)
tk.Button(root, text='2', padx=20, pady=20, font=('Arial', 14), command=lambda: press(2)).grid(row=3, column=1)
tk.Button(root, text='3', padx=20, pady=20, font=('Arial', 14), command=lambda: press(3)).grid(row=3, column=2)
tk.Button(root, text='-', padx=20, pady=20, font=('Arial', 14), command=lambda: press('-')).grid(row=3, column=3)

# Buttons (0, ., =, +)
tk.Button(root, text='0', padx=20, pady=20, font=('Arial', 14), command=lambda: press(0)).grid(row=4, column=0)
tk.Button(root, text='.', padx=22, pady=20, font=('Arial', 14), command=lambda: press('.')).grid(row=4, column=1)
tk.Button(root, text='=', padx=20, pady=20, font=('Arial', 14), command=equalpress).grid(row=4, column=2)
tk.Button(root, text='+', padx=20, pady=20, font=('Arial', 14), command=lambda: press('+')).grid(row=4, column=3)

# Clear button
tk.Button(root, text='C', padx=95, pady=20, font=('Arial', 14), command=clear).grid(row=5, column=0, columnspan=4)

# Start the main event loop
root.mainloop()
