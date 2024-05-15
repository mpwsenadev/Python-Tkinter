import tkinter as tk
from tkinter import messagebox
import random

class AdivinharNumero:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo de Adivinhação")
        self.master.geometry("300x200")
        self.master.configure(bg="#f0f0f0")
        
        self.target_number = random.randint(1, 50)
        
        self.title_label = tk.Label(master, text="Adivinhe o Número", font=("Arial", 16), bg="#f0f0f0")
        self.title_label.pack(pady=10)
        
        self.info_label = tk.Label(master, text="Digite um número entre 1 e 50:", font=("Arial", 10), bg="#f0f0f0")
        self.info_label.pack()
        
        self.guess_entry = tk.Entry(master, font=("Arial", 12), width=10)
        self.guess_entry.pack(pady=5)
        
        self.guess_button = tk.Button(master, text="Adivinhar", font=("Arial", 12), command=self.check_guess)
        self.guess_button.pack(pady=5)
        
        self.reset_button = tk.Button(master, text="Reiniciar", font=("Arial", 12), command=self.reset_game)
        self.reset_button.pack(pady=5)
        
    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if guess == self.target_number:
                messagebox.showinfo("Parabéns!", "Você adivinhou o número!")
            elif guess < self.target_number:
                messagebox.showinfo("Dica", "Tente um número maior.")
            else:
                messagebox.showinfo("Dica", "Tente um número menor.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")
        
    def reset_game(self):
        self.target_number = random.randint(1, 50)
        self.guess_entry.delete(0, tk.END)
        
def main():
    root = tk.Tk()
    root.configure(bg="#f0f0f0")
    game = AdivinharNumero(root)
    root.mainloop()

if __name__ == "__main__":
    main()
