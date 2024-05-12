import tkinter as tk
from tkinter import messagebox

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Por favor, insira uma tarefa.")

def remover_tarefa():
    try:
        indice = lista_tarefas.curselection()[0]
        lista_tarefas.delete(indice)
    except IndexError:
        messagebox.showwarning("Atenção", "Selecione uma tarefa para remover.")

def limpar_tarefas():
    lista_tarefas.delete(0, tk.END)

root = tk.Tk()
root.title("Lista de Tarefas")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

entrada_tarefa = tk.Entry(frame_input, font=("Helvetica", 14))
entrada_tarefa.pack(side=tk.LEFT, ipadx=30, padx=5)

botao_adicionar = tk.Button(frame_input, text="Adicionar Tarefa", font=("Helvetica", 12), command=adicionar_tarefa)
botao_adicionar.pack(side=tk.LEFT, padx=5)

frame_lista = tk.Frame(root)
frame_lista.pack(padx=10, pady=5)

scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_tarefas = tk.Listbox(frame_lista, width=50, height=15, font=("Helvetica", 12), yscrollcommand=scrollbar.set)
lista_tarefas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
scrollbar.config(command=lista_tarefas.yview)

frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)

botao_remover = tk.Button(frame_botoes, text="Remover Tarefa", font=("Helvetica", 12), command=remover_tarefa)
botao_remover.pack(side=tk.LEFT, padx=5)

botao_limpar = tk.Button(frame_botoes, text="Limpar Tarefas", font=("Helvetica", 12), command=limpar_tarefas)
botao_limpar.pack(side=tk.LEFT, padx=5)

root.mainloop()
