import os
import json
import tkinter as tk
from tkinter import messagebox, ttk

class SistemaJovensGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Arquivos Jovens 4.0")
        self.root.geometry("500x550")
        self.configurar_sistema()

        # Interface - Título
        tk.Label(root, text="SISTEMA DE UPLOAD JSON", font=("Arial", 16, "bold")).pack(pady=10)

        # Campos de Entrada
        tk.Label(root, text="Nome do Aluno:").pack()
        self.ent_nome = tk.Entry(root, width=50)
        self.ent_nome.pack(pady=5)

        tk.Label(root, text="Resumo do Projeto:").pack()
        self.txt_projeto = tk.Text(root, height=5, width=38)
        self.txt_projeto.pack(pady=5)

        # Botões Principais
        tk.Button(root, text="Salvar / Atualizar Projeto", command=self.salvar_projeto, bg="green", fg="white").pack(pady=5)
        tk.Button(root, text="Listar Projetos", command=self.atualizar_lista).pack(pady=5)

        # Lista de Projetos (Visual)
        tk.Label(root, text="Projetos na Pasta:").pack(pady=10)
        self.lista_visual = tk.Listbox(root, width=50, height=8)
        self.lista_visual.pack(pady=5)
        self.lista_visual.bind('<<ListboxSelect>>', self.carregar_selecionado)

        self.atualizar_lista()

    def configurar_sistema(self):
        if not os.path.exists("uploads_projetos"):
            os.makedirs("uploads_projetos")

    def salvar_projeto(self):
        nome = self.ent_nome.get().strip()
        projeto = self.txt_projeto.get("1.0", tk.END).strip()

        if not nome or not projeto:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        dados = {"aluno": nome, "projeto": projeto}
        nome_fich = nome.replace(" ", "_").lower()
        caminho = f"uploads_projetos/projeto_{nome_fich}.json"

        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        
        messagebox.showinfo("Sucesso", f"Projeto de {nome} salvo!")
        self.limpar_campos()
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_visual.delete(0, tk.END)
        arquivos = [f for f in os.listdir("uploads_projetos") if f.endswith(".json")]
        for f in arquivos:
            self.lista_visual.insert(tk.END, f)

    def carregar_selecionado(self, event):
        selecao = self.lista_visual.curselection()
        if selecao:
            nome_arquivo = self.lista_visual.get(selecao)
            with open(f"uploads_projetos/{nome_arquivo}", "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.limpar_campos()
                self.ent_nome.insert(0, dados['aluno'])
                self.txt_projeto.insert("1.0", dados['projeto'])

    def limpar_campos(self):
        self.ent_nome.delete(0, tk.END)
        self.txt_projeto.delete("1.0", tk.END)

# Iniciar App
if __name__ == "__main__":
    janela = tk.Tk()
    app = SistemaJovensGUI(janela)
    janela.mainloop()