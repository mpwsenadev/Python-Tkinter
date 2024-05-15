import tkinter as tk
import random

def move_button():
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    button_width = button.winfo_width()
    button_height = button.winfo_height()
    new_x = random.randint(0, window_width - button_width)
    new_y = random.randint(0, window_height - button_height)
    button.place(x=new_x, y=new_y)

root = tk.Tk()
root.title("Click the Button")
root.geometry("600x400")

button = tk.Button(root, text="Clique-me!", command=move_button)
button.place(x=250, y=150)

root.mainloop()
