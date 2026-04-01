# 1. Função para ESCREVER (Gravar dados)
def escrever_no_arquivo():
    print('--- Sistema de upload dos arquivos jovens ---')
    novo_nome = input("Digite o nome do jovem para cadastrar: ")

    # Usamos 'a' (append) para ADICIONAR ao final do arquivo sem apagar o que já existe
    with open('arquivo_lido.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(novo_nome + "\n") # O \n pula para a próxima linha
    
    print(f"Sucesso! {novo_nome} foi salvo.")

# 2. Função para LER (Mostrar dados)
def ler_arquivo_jovens():
    print('\n--- Lendo arquivo atualizado ---')
    with open('arquivo_lido.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

# --- Execução ---
escrever_no_arquivo()
ler_arquivo_jovens()