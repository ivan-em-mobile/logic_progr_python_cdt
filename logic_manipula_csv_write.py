import csv

#   csv.writer() para escrever em arquivos CSV.

dados = [["Nome", "Idade"], ["Maria", 25], 
         ["Joao", 30], ["Andre", 19], 
         ["Fabricio", 21]] 

with open("dados.csv", "w", newline="") as arquivo: 
    
    escritor = csv.writer(arquivo)
    
    escritor.writerows(dados) 
    
    print(dados) 



