import customtkinter as ctk

def on_button_click():
    message_label.configure(text="Olá Mundo")

app = ctk.CTk()
app.geometry("300x200")
app.title("Olá Mundo")

button = ctk.CTkButton(app, text="Clique Aqui", command=on_button_click)
button.pack(pady=20)

message_label = ctk.CTkLabel(app, text="")
message_label.pack(pady=20)

app.mainloop()
