import tkinter as tk
import random
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def on_click(event):
    distance = calculate_distance(event.x, event.y, treasure_x, treasure_y)
    if distance < 20:
        message.config(text="Tesouro encontrado!", fg="green")
        canvas.create_text(event.x, event.y, text="", font=("Helvetica", 24), fill="gold")
    elif distance < 100:
        message.config(text="Quente!", fg="red")
        canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="red")
    else:
        message.config(text="Frio!", fg="blue")
        canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="blue")

root = tk.Tk()
root.title("Caça ao Tesouro")
root.geometry("800x600")
root.configure(bg="lightblue")
root.option_add('*Font', 'Helvetica 14')

treasure_x = random.randint(50, 750)
treasure_y = random.randint(50, 550)

message = tk.Label(root, text="Clique para encontrar o tesouro!", font=("Helvetica", 18, "bold"), bg="lightblue")
message.pack(pady=20)

canvas = tk.Canvas(root, width=800, height=500, bg="lightyellow", cursor="trek")
canvas.pack()

root.bind('<Button-1>', on_click)

root.mainloop()
