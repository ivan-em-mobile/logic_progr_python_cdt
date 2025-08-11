import csv

nome_arquivo = 'manipula.csv'

with open("manipula.csv","r" ) as arquivo:
    
    leitor = csv.reader(arquivo)
    
    # for coluna in leitor:
    #     print(coluna)
    
    for linha in leitor:
        print(linha)



