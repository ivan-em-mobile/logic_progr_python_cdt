import tkinter as tk
from tkinter import messagebox
from collections import deque # Importa deque para gerenciar o histórico de forma eficiente

# Variável global para armazenar as últimas 20 médias
# deque(maxlen=20) garante que a lista NUNCA terá mais de 20 itens.
historico_medias = deque(maxlen=20)

# Lista para referenciar os campos de entrada (Entry widgets)
# Será populada na função main
campos_entrada = []

# 1. Função para calcular a média das notas
def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas."""
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

# 2. Função para Limpar a Última Nota (NOVA FUNÇÃO)
def limpar_ultima_nota():
    """Limpa o texto do último campo de entrada de nota."""
    if campos_entrada:
        # Pega o último campo da lista de campos e limpa seu conteúdo
        ultimo_campo = campos_entrada[-1]
        ultimo_campo.delete(0, tk.END) # Deleta do índice 0 até o final
        messagebox.showinfo("Limpar", "A última nota foi limpa. Por favor, digite o novo valor.")
    else:
        messagebox.showwarning("Atenção", "Nenhum campo de nota encontrado.")


# 3. Lógica de Cadastro e Cálculo
def cadastrar_e_calcular():
    global historico_medias
    
    notas = []
    
    try:
        # Tenta converter o texto de cada campo para float.
        for campo in campos_entrada:
            valor_str = campo.get().strip().replace(',', '.') 
            
            # Se o campo estiver vazio, considera um erro
            if not valor_str:
                messagebox.showerror("Erro de Entrada", "Por favor, preencha todas as 3 notas.")
                return
            
            valor_nota = float(valor_str)
            
            # Validação simples de nota
            if 0 <= valor_nota <= 10:
                notas.append(valor_nota)
            else:
                messagebox.showerror("Erro de Validação", "As notas devem estar entre 0 e 10 (0 a 10).")
                return
                
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Valores inválidos. Digite apenas números.")
        return

    # Cálculo e Histórico (PARTE ATUALIZADA)
    media_final = calcular_media(notas)
    
    # Adiciona a nova média ao histórico. Se o histórico já tiver 20 itens, o mais antigo é removido.
    historico_medias.append(media_final) 
    
    # 4. Exibir Resultado
    nota_minima_aprovacao = 7.0
    resultado_texto = f"Média Calculada: {media_final:.2f}\n"
    
    if media_final >= nota_minima_aprovacao:
        resultado_texto += "STATUS: 🎉 ALUNO APROVADO!"
        titulo_caixa = "Resultado: APROVADO"
    else:
        resultado_texto += "STATUS: 😢 ALUNO REPROVADO."
        titulo_caixa = "Resultado: REPROVADO"
        
    messagebox.showinfo(titulo_caixa, resultado_texto)
    
    # Opcional: Limpa os campos após o cálculo para o próximo cadastro
    for campo in campos_entrada:
        campo.delete(0, tk.END)

# 5. Função para Mostrar o Histórico (NOVA FUNÇÃO)
def mostrar_historico():
    """Exibe as últimas 20 médias calculadas."""
    if not historico_medias:
        mensagem = "Ainda não há médias calculadas para exibir no histórico."
    else:
        # Cria uma string formatada com todas as médias
        historico_formatado = [f"- Média: {m:.2f}" for m in historico_medias]
        # Conta quantos itens estão atualmente no deque
        total_historico = len(historico_medias)
        
        mensagem = (
            f"--- Histórico das Últimas {total_historico} Médias ---\n\n"
            + "\n".join(historico_formatado)
        )
    
    messagebox.showinfo("Histórico de Médias", mensagem)


# --- Configuração da Interface Gráfica (GUI) ---
if __name__ == "__main__":
    
    janela = tk.Tk()
    janela.title("Sistema de Cálculo de Notas (GUI)")
    janela.geometry("400x280")
    
    # Configuração da Barra de Menu
    menu_bar = tk.Menu(janela)
    janela.config(menu=menu_bar)
    
    # Menu "Arquivo"
    menu_arquivo = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)
    menu_arquivo.add_command(label="Cadastrar Notas", command=cadastrar_e_calcular)
    menu_arquivo.add_command(label="Mostrar Histórico (20)", command=mostrar_historico) # Opção para Histórico
    menu_arquivo.add_separator()
    menu_arquivo.add_command(label="Sair", command=janela.quit)

    # Widgets da Tela Principal
    tk.Label(janela, text="Insira as Notas (0 a 10):", font=('Arial', 10, 'bold')).grid(row=0, column=0, columnspan=3, pady=10)
    
    # Criação dos campos de entrada
    
    # Nota 1
    tk.Label(janela, text="Nota 1:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
    entry_nota1 = tk.Entry(janela, width=15)
    entry_nota1.grid(row=1, column=1, padx=5, pady=5)
    
    # Nota 2
    tk.Label(janela, text="Nota 2:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
    entry_nota2 = tk.Entry(janela, width=15)
    entry_nota2.grid(row=2, column=1, padx=5, pady=5)
    
    # Nota 3
    tk.Label(janela, text="Nota 3:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
    entry_nota3 = tk.Entry(janela, width=15)
    entry_nota3.grid(row=3, column=1, padx=5, pady=5)
    
    # Popula a lista de campos (IMPORTANTE para as funções limpar_ultima_nota e calcular)
    campos_entrada = [entry_nota1, entry_nota2, entry_nota3]
    
    # Botão para Acionar o Cálculo
    tk.Button(janela, text="Calcular Média", command=cadastrar_e_calcular, bg='#4CAF50', fg='white', font=('Arial', 10, 'bold')).grid(row=4, column=0, columnspan=2, pady=10)
    
    # NOVO BOTÃO: Limpar Última Nota
    tk.Button(janela, text="Limpar Última Nota", command=limpar_ultima_nota, bg='#FF9800', fg='white').grid(row=5, column=0, columnspan=2, pady=5)

    janela.mainloop()