'''
explicação Manhã
'''

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("400x300")

def click_login():
    print("Botão de login clicado")

janela.title("Explicação do Módulo Pacote GUI")

texto = customtkinter.CTkLabel(janela, text="Tela de fazer login")

email = customtkinter.CTkEntry(janela, placeholder_text="Digite seu email")

botao_login = customtkinter.CTkButton(janela, text="Login", command=click_login)

texto.pack(pady=10, padx=10)
email.pack(pady=10, padx=10)
botao_login.pack(pady=10, padx=10)

janela.mainloop()