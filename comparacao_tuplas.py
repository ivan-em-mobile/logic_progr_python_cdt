print("--- Gerenciador de Tarefas Fixas (Tupla) ---\n")

# Uma tupla de tarefas. Note os parênteses `()`.
tarefas = ("Reunião com o cliente", "Preparar relatório", "Enviar e-mails", "Acompanhar feedback")

print("Tarefas atuais:")
for i, tarefa in enumerate(tarefas):
    print(f"{i + 1}. {tarefa}")

# --- Loop Principal do Programa ---
while True:
    print("\n--- Opções ---")
    print("1 - Listar tarefas")
    print("2 - Adicionar uma nova tarefa (cria nova tupla)")
    print("3 - Remover uma tarefa (cria nova tupla)")
    print("4 - Sair")

    opcao = input("Digite sua opção: ")

    if opcao == "1":
        print("\n--- Tarefas Atuais ---")
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i + 1}. {tarefa}")
        print("--------------------")

    elif opcao == "2":
        nova_tarefa = input("Digite a nova tarefa a ser adicionada: ")
        # Para "adicionar" em uma tupla, criamos uma nova tupla
        # com os elementos antigos mais o novo.
        # A vírgula depois de 'nova_tarefa' é crucial para que seja tratada como tupla.
        tarefas = tarefas + (nova_tarefa.strip(),)
        print(f"'{nova_tarefa.strip()}' foi adicionada à lista de tarefas.")

    elif opcao == "3":
        if not tarefas:
            print("A lista de tarefas está vazia. Nada para remover.")
            continue # Volta para o início do loop

        print("\n--- Tarefas para Remover ---")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1}. {tarefa}")
        try:
            indice_remover = int(input("Digite o NÚMERO da tarefa a ser removida: ")) - 1
            if 0 <= indice_remover < len(tarefas):
                # Para "remover" de uma tupla, criamos uma nova tupla
                # excluindo o elemento no índice especificado.
                # Fatiamos a tupla: tudo antes do índice + tudo depois do índice.
                tarefas = tarefas[:indice_remover] + tarefas[indice_remover+1:]
                print("Tarefa removida com sucesso!")
            else:
                print("Número de tarefa inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


    elif opcao == "4":
        print("Saindo do gerenciador de tarefas... Adeus!")
        break

    else:
        print("Opção inválida. Tente novamente.")