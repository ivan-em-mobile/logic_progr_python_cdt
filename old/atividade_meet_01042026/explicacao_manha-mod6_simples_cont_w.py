def sobrescrever_arquivo():
    print('--- Sistema de upload dos arquivos jovens (Modo Sobrescrever) ---')
    
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