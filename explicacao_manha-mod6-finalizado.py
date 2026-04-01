'''
print('Sistema de upload dos arquivos jovens')

def ler_txt(arquivo_lido): #É Uma função definida pelo usuario
# def ler_txt(caminho_arquivo): #É Uma função definida pelo usuario

    try: #tratamento de erro dos arquivos
        # 'with' garante que o ficheiro é fechado automaticamente

        with open(arquivo_lido, 'r', encoding='utf-8') as arquivo:
        # with open(caminho_arquivo, 'r', encoding='utf-8') as ficheiro:

            conteudo = arquivo.read()

            return conteudo
        
    except FileNotFoundError:#resposta dos erro

        return "Erro: Ficheiro não encontrado."

# Exemplo de uso:
# texto = ler_txt("arquivo_lido.txt")
# print(texto)


# Função para ler o arquivo
def ler_arquivo_jovens():
    print('Sistema de upload dos arquivos jovens')
    print('-' * 30)

# try

    # Abrimos o arquivo 'arquivo_lido.txt' apenas para leitura ('r')
    with open('arquivo_lido.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read() # Guarda tudo o que está no texto numa variável
        print(conteudo)           # Mostra o conteúdo na tela

# Chamar a função para ela funcionar
ler_arquivo_jovens()

#except
'''

def sobrescrever_arquivo():
    print('--- Sistema de upload dos arquivos jovens (Modo Sobrescrever) ---')
    print('-' * 60)
    
    # Pedimos o novo conteúdo
    conteudo_novo = input("Digite o que deseja salvar (ISSO APAGARÁ O QUE ESTAVA LÁ): ")

    # Usamos 'w' para escrever. Se o arquivo já existir, ele será "resetado".
    with open('arquivo_lido.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo_novo + "\n")
    
    print("\n[AVISO] O arquivo foi limpo e o novo conteúdo foi gravado!")

def ler_arquivo_jovens(): 
    print('\n--- Lendo o arquivo agora ---')
    try:
        with open('arquivo_lido.txt', 'r', encoding='utf-8') as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Arquivo ainda não existe.")

# --- Execução ---
sobrescrever_arquivo()
ler_arquivo_jovens()
