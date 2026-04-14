import os

def configurar_ambiente():
    """Garante que o arquivo de exemplo exista para o teste."""
    nome_arquivo = "arquivo_lido.txt"
    if not os.path.exists(nome_arquivo):
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write("Lista de Alunos Jovens:\n1. Ana\n2. Bruno\n3. Carlos")
        print(f">> Arquivo '{nome_arquivo}' criado para teste.")

def ler_arquivo_jovens(caminho):
    """
    Lê o conteúdo do arquivo e retorna uma lista de linhas.
    Aplica o conceito de tratamento de exceções.
    """
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            # .readlines() transforma cada linha do TXT em um item de uma lista
            conteudo = arquivo.readlines()
            return conteudo
    except FileNotFoundError:
        print(f"[ERRO] O arquivo '{caminho}' não foi encontrado na pasta.")
        return None

def exibir_upload_sucesso(dados):
    """Formata e exibe os dados lidos na tela."""
    print('\n' + '='*40)
    print('   CONTEÚDO DO ARQUIVO LIDO   ')
    print('='*40)
    
    if dados:
        for linha in dados:
            # .strip() remove o '\n' (quebra de linha) invisível no final
            print(f"-> {linha.strip()}")
    else:
        print("O arquivo está vazio ou não pôde ser lido.")
    
    print('='*40)

# --- EXECUÇÃO PRINCIPAL ---
ARQUIVO = "arquivo_lido.txt"

configurar_ambiente() # Apenas para garantir que o arquivo existe
dados_lidos = ler_arquivo_jovens(ARQUIVO)

if dados_lidos:
    exibir_upload_sucesso(dados_lidos)