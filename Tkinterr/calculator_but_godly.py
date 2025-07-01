import tkinter as tk
import math

allowed_functions = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
    "log": math.log10,
    "ln": math.log,
    "pi": math.pi,
    "e": math.e,
    "abs": abs,
    "pow": pow
}

expression = ""

def safe_eval(expr):
    expr = expr.replace("^", "**")
    expr = expr.replace("%", "/100")
    return eval(expr, {"__builtins__": None}, allowed_functions)

def press(char):
    global expression
    expression += str(char)
    equation.set(expression)
    update_preview()

def update_preview():
    try:
        result = safe_eval(expression)
        preview.set("= " + str(result))
    except:
        preview.set("")

def equalpress():
    global expression
    try:
        result = safe_eval(expression)
        equation.set(str(result))
        preview.set("")
        expression = str(result)
    except:
        equation.set("Error")
        expression = ""
        preview.set("")

def clear():
    global expression
    expression = ""
    equation.set("")
    preview.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)
    update_preview()

def key_event(event):
    key = event.keysym
    char = event.char
    if key in ("Return", "Equal"):
        equalpress()
    elif key == "BackSpace":
        backspace()
    elif key in ("Escape", "Delete", "Clear"):
        clear()
    elif char in "0123456789+-*/().^%":
        press(char)
    elif char.lower() in "sctlpe":
        pass

root = tk.Tk()
root.title("Ultimate Calculator")
root.geometry("420x570")
root.configure(bg="#1e1e2f")

equation = tk.StringVar()
preview = tk.StringVar()

entry = tk.Entry(root, textvariable=equation, font=('Consolas', 24),
                 bd=10, insertwidth=2, width=22, borderwidth=4, justify='right',
                 bg="#2d2d44", fg="white")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=12, pady=5)
entry.focus_set()

tk.Label(root, textvariable=preview, font=('Consolas', 16), fg="lightgray",
         bg="#1e1e2f", anchor="e").grid(row=1, column=0, columnspan=4, sticky="we")

def create_btn(text, row, col, cmd=None, colspan=1, bg="#3b3b5c", fg="white"):
    if cmd is None:
        cmd = lambda t=text: press(t)
    tk.Button(root, text=text, font=('Consolas', 16), padx=20, pady=20,
              bg=bg, fg=fg, activebackground="#5c5c8a", command=cmd)\
        .grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

buttons = [
    [("C", clear, "#607d8b"), ("⌫", backspace, "#607d8b"), ("%",), ("/",)],
    [("7",), ("8",), ("9",), ("*",)],
    [("4",), ("5",), ("6",), ("-",)],
    [("1",), ("2",), ("3",), ("+",)],
    [("0",), (".",), ("^",), ("=", equalpress, "#4caf50")],
    [("(",), (")",), ("pi",), ("e",)],
    [("sin",), ("cos",), ("tan",), ("sqrt",)],
    [("log",), ("ln",), ("abs",), ("pow",)],
]

for i, row in enumerate(buttons, start=2):
    for j, btn in enumerate(row):
        if len(btn) == 1:
            create_btn(btn[0], i, j)
        elif len(btn) == 2:
            create_btn(btn[0], i, j, btn[1])
        elif len(btn) == 3:
            create_btn(btn[0], i, j, btn[1], 1, btn[2])

for i in range(len(buttons) + 2):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

root.bind("<Key>", key_event)
root.mainloop()
