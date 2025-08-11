import csv

#  biblioteca csv para ler arquivos CSV

nome_arquivo = 'manipula.csv'

with open("manipula.csv","r" ) as arquivo:
    
    leitor = csv.reader(arquivo)  
    
    for linha in leitor:
        
        print(linha)