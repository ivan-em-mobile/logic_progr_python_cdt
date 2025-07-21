def menu():
    print("\n#### MENU ####")
    print("1. Adicionar nome")
    print("2. Remover nome")
    print("3. Sair")

nome = input("Digite o nome: ").split(", ")
nomes = [nomes.strip() for nomes in nome]

while True:
    menu()
    escolha = input("Escolha uma opção (1 a 3): ")

    if escolha == "3":
        print("Saindo...")
        break

    elif escolha == "1":
        nome = input("Digite o nome para adicionar: ")
        nomes.append(nome)
        print(f"Nome '{nome}' adicionado.")
        print("Lista atualizada:", nomes)

    elif escolha == "2":
        nome = input("Digite o nome para remover: ")
        if nome in nomes:
            nomes.remove(nome)
            print(f"Nome '{nome}' removido.")
        else:
            print(f"Nome '{nome}' não encontrado na lista.")
        print("Lista atualizada:", nomes)

    else:
        print("Opção inválida. Por favor, escolha entre 1 e 3.")
