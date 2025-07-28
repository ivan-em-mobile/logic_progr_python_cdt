print("--- Gerenciador de Participantes (Conjunto) ---\n")

# Um conjunto vazio para armazenar os nomes dos participantes.
# Note as chaves `{}` sem pares chave-valor para um conjunto vazio, ou com itens separados por vírgula.
participantes = set()

print("Bem-vindo ao Gerenciador de Participantes!")

# --- Loop Principal do Programa ---
while True:
    print("\n--- Opções ---")
    print("1 - Adicionar participante")
    print("2 - Remover participante")
    print("3 - Listar participantes")
    print("4 - Sair")

    opcao = input("Digite sua opção: ")

    if opcao == "1":
        # Opção 1: Adicionar participante
        novo_participante = input("Digite o nome do participante a adicionar: ")
        # O método 'add()' adiciona um item ao conjunto. Se já existir, nada acontece.
        participantes.add(novo_participante.strip())
        print(f"'{novo_participante.strip()}' foi adicionado (se não existia).")

    elif opcao == "2":
        # Opção 2: Remover participante
        participante_remover = input("Digite o nome do participante a remover: ")
        if participante_remover.strip() in participantes:
            # O método 'remove()' remove um item do conjunto.
            participantes.remove(participante_remover.strip())
            print(f"'{participante_remover.strip()}' foi removido.")
        else:
            print(f"'{participante_remover.strip()}' não está na lista de participantes.")

    elif opcao == "3":
        # Opção 3: Listar participantes
        print("\n--- Participantes Cadastrados ---")
        if not participantes:
            print("Nenhum participante cadastrado.")
        else:
            # Iterar sobre um conjunto não garante ordem, pois são não ordenados.
            for participante in sorted(list(participantes)): # Opcional: ordenar para exibir.
                print(f"- {participante}")
        print("---------------------------------")

    elif opcao == "4":
        print("Saindo do Gerenciador de Participantes... Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")