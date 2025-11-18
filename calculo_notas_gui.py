import tkinter as tk
from tkinter import messagebox

# 1. Documentação: Função para calcular a média das notas
# Esta função continua sendo o coração da lógica de cálculo.
def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas."""
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

# 2. Lógica de Cadastro e Cálculo (Conectada ao Botão da GUI)
def cadastrar_e_calcular():
    # As notas são obtidas dos campos de entrada (Entry) da GUI.
    
    # Lista para armazenar as notas que serão convertidas.
    notas = []
    
    # Lista de campos de entrada (globalmente definidas no __main__)
    campos = [entry_nota1, entry_nota2, entry_nota3]
    
    try:
        # Tenta converter o texto de cada campo para float.
        for campo in campos:
            # Pega o texto do campo e remove espaços em branco.
            valor_str = campo.get().strip().replace(',', '.') 
            if not valor_str:
                messagebox.showerror("Erro de Entrada", "Por favor, preencha todas as 3 notas.")
                return
            
            valor_nota = float(valor_str)
            
            # Validação simples de nota
            if 0 <= valor_nota <= 10:
                notas.append(valor_nota)
            else:
                messagebox.showerror("Erro de Validação", "As notas devem estar entre 0 e 10.")
                return
                
    except ValueError:
        # Captura erro se a conversão para float falhar (ex: texto digitado).
        messagebox.showerror("Erro de Entrada", "Valores inválidos. Digite apenas números.")
        return

    # 3. Cálculo e Retorno de Status
    media_final = calcular_media(notas)
    nota_minima_aprovacao = 7.0
    
    # Formatação da mensagem de resultado
    resultado_texto = f"Média Calculada: {media_final:.2f}\n"
    
    if media_final >= nota_minima_aprovacao:
        resultado_texto += "STATUS: 🎉 ALUNO APROVADO!"
        titulo_caixa = "Resultado: APROVADO"
    else:
        resultado_texto += "STATUS: 😢 ALUNO REPROVADO."
        titulo_caixa = "Resultado: REPROVADO"
        
    # Exibe o resultado final em uma caixa de mensagem.
    messagebox.showinfo(titulo_caixa, resultado_texto)
    
# --- Configuração da Interface Gráfica (GUI) ---
if __name__ == "__main__":
    
    # 1. Configuração da Janela Principal
    janela = tk.Tk()
    janela.title("Sistema de Cálculo de Notas (GUI)")
    janela.geometry("350x200") # Define o tamanho inicial da janela
    
    # 2. Criação da Barra de Menu (Menu Bar)
    menu_bar = tk.Menu(janela)
    janela.config(menu=menu_bar)
    
    # Menu "Arquivo"
    menu_arquivo = tk.Menu(menu_bar, tearoff=0) # tearoff=0 remove a linha tracejada
    menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)
    
    # Opções do menu "Arquivo"
    # A opção "Cadastrar Notas" chama a função principal de cálculo, que é o que o programa faz.
    # Poderíamos abrir uma nova janela, mas para este projeto simples, a tela principal é o cadastro.
    menu_arquivo.add_command(label="Cadastrar Notas", command=cadastrar_e_calcular) 
    menu_arquivo.add_separator()
    # Opção "Sair"
    menu_arquivo.add_command(label="Sair", command=janela.quit)
    
    # 3. Widgets da Tela Principal (Layout)
    
    tk.Label(janela, text="Insira as Notas do Aluno (0 a 10):", font=('Arial', 10, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
    
    # Labels e Campos de Entrada para 3 Notas
    tk.Label(janela, text="Nota 1:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
    entry_nota1 = tk.Entry(janela, width=15)
    entry_nota1.grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(janela, text="Nota 2:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
    entry_nota2 = tk.Entry(janela, width=15)
    entry_nota2.grid(row=2, column=1, padx=5, pady=5)
    
    tk.Label(janela, text="Nota 3:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
    entry_nota3 = tk.Entry(janela, width=15)
    entry_nota3.grid(row=3, column=1, padx=5, pady=5)
    
    # Botão para Acionar o Cálculo
    tk.Button(janela, text="Calcular Média", command=cadastrar_e_calcular, bg='#4CAF50', fg='white', font=('Arial', 10, 'bold')).grid(row=4, column=0, columnspan=2, pady=10)

    # Inicia o loop principal da interface gráfica
    janela.mainloop()