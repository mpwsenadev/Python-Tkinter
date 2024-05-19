import customtkinter as ctk
from tkinter import END
import tkinter as tk

def btn_click(item):
    current_text = entry.get()
    entry.delete(0, END)
    entry.insert(END, current_text + str(item))

def btn_clear():
    entry.delete(0, END)

def btn_equal():
    result = ""
    try:
        result = str(eval(entry.get()))
    except:
        result = "Erro"
    entry.delete(0, END)
    entry.insert(END, result)

root = ctk.CTk()
root.title("Calculadora")
root.geometry("400x550")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = (screen_width/2) - (400/2)
y_coordinate = (screen_height/2) - (550/2)

root.geometry(f"400x550+{int(x_coordinate)}+{int(y_coordinate)}")

entry = ctk.CTkEntry(root, width=380, height=60, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        ctk.CTkButton(root, text=button, width=90, height=90, command=btn_equal).grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        ctk.CTkButton(root, text=button, width=90, height=90, command=lambda button=button: btn_click(button)).grid(row=row_val, column=col_val, padx=5, pady=5)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

ctk.CTkButton(root, text='C', width=380, height=50, command=btn_clear).grid(row=row_val, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()
