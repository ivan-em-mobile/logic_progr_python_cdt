# Função para ler o arquivo
def ler_arquivo_jovens():
    print('Sistema de upload dos arquivos jovens')
    print('-' * 30)

    # Abrimos o arquivo 'arquivo_lido.txt' apenas para leitura ('r')
    with open('arquivo_lido.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read() # Guarda tudo o que está no texto numa variável
        print(conteudo)           # Mostra o conteúdo na tela

# Chamar a função para ela funcionar
ler_arquivo_jovens()