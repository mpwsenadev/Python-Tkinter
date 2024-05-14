import tkinter as tk
import string
import random

def generate_password():
    length = int(length_entry.get())
    if length <= 0:
        password_var.set("Comprimento inválido")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_var.set(password)

root = tk.Tk()
root.title("Gerador de Senha")
root.geometry("300x250")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

password_var = tk.StringVar()

main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(expand=True, fill="both")

title_label = tk.Label(main_frame, text="Gerador de Senha", font=("Arial", 18), bg="#f0f0f0")
title_label.pack(pady=(20, 10))

input_frame = tk.Frame(main_frame, bg="#f0f0f0")
input_frame.pack()

length_label = tk.Label(input_frame, text="Comprimento:", font=("Arial", 12), bg="#f0f0f0")
length_label.grid(row=0, column=0, padx=(10, 5), pady=10)

length_entry = tk.Entry(input_frame, font=("Arial", 12), bd=2, relief="solid", width=5)
length_entry.grid(row=0, column=1, padx=(0, 10), pady=10)
length_entry.insert(0, "8")

generate_button = tk.Button(main_frame, text="Gerar Senha", font=("Arial", 12), bg="#4caf50", fg="white", relief="flat", command=generate_password)
generate_button.pack(pady=10, ipadx=10, ipady=5)

password_label = tk.Label(main_frame, textvariable=password_var, font=("Arial", 12), bg="#f0f0f0", wraplength=280, justify="center")
password_label.pack()

root.mainloop()
