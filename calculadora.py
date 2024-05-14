import tkinter as tk

def add_to_display(value):
    current = display_var.get()
    if current == "0":
        display_var.set(value)
    else:
        display_var.set(current + value)

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except:
        display_var.set("Error")

def clear_display():
    display_var.set("0")

root = tk.Tk()
root.title("Calculadora")
root.geometry("300x400")

display_var = tk.StringVar()
display_var.set("0")

display_frame = tk.Frame(root, bg="lightgray", bd=5)
display_frame.pack(fill=tk.BOTH, expand=True)

display = tk.Label(display_frame, textvariable=display_var, anchor="e", bg="white", font=("Arial", 20))
display.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("+", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("-", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("*", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("=", 3, 2), ("/", 3, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(button_frame, text=text, font=("Arial", 20), command=lambda t=text: add_to_display(t))
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

clear_button = tk.Button(button_frame, text="C", font=("Arial", 20), command=clear_display)
clear_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

equal_button = tk.Button(button_frame, text="=", font=("Arial", 20), command=calculate)
equal_button.grid(row=4, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

for i in range(4):
    button_frame.rowconfigure(i, weight=1)
    button_frame.columnconfigure(i, weight=1)

root.mainloop()
