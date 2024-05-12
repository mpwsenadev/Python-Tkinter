import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Olá! Você clicou no botão.")

root = tk.Tk()
root.title("Exemplo Tkinter")

botao = tk.Button(root, text="Clique aqui", command=mostrar_mensagem)
botao.pack(pady=10)

root.mainloop()
