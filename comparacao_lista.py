###Criando uma lista
##Ivan, Gustavo, 
# Tarso, Fabricio, 
# Rafa-Gatao, 
# Gabriel, Victor, Renan

#Qual seria o print e 
# input para pedir os nomes?

print("*** Lista de Nomes ***\n")

nomes = input("Digite os nomes separados por vírgula: ").split(", ")

#nomes = [nome.strip() for nome in nomes]

#print(nomes)

print("\n Quais operações você quer fazer:")
print("1 - Adicionar um nome")
print("2 - Remover um nome")
print("3 - Listar nomes")
print("4 - Sair")

#faça um loop para pedir a opção do usuário
while True:
    
    opcao = input("\nDigite a opção desejada (1-4): ")
 
    if opcao == "1":
        novo_nome = input("Digite o nome a ser adicionado: ")
        nomes.append(novo_nome)
        print(f"{novo_nome} foi adicionado à lista.")
        #print(f" foi adicionado à lista.")
    
    elif opcao == "2":
        nome_remover = input("Digite o nome a ser removido: ")
        if nome_remover in nomes:
            nomes.remove(nome_remover)
            print(f"{nome_remover} foi removido da lista.")
        else:
            print(f"{nome_remover} não está na lista.")
        #print(f" não está na lista.")    
    
    elif opcao == "3":
        print("\nLista de Nomes:")
        for nome in nomes:
            print(nome)
    
    elif opcao == "4":
        print("Você saiu do programa - EXIT.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")