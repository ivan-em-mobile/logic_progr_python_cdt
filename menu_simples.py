
def apresentacao():

    print("Seja bem-vindo(a) ao Banco MMS! - Plus ultra")
    print("-" * 20) # Imprime 20 hífens para criar uma linha divisória

    print("Veja as opções a seguir:\n" # O '\n' serve para pular uma linha
          "1 - Conta Corrente \n"
          "2 - Conta Poupança\n"
          "3 - Encerrar sistema")
    print("-" * 20)

def logica_escolha():
    """
    Controla o que acontece depois que o usuário escolhe uma opção.
    Fica em loop até o usuário escolher '3' para sair.
    """
    while True: # 'while True' significa que o código dentro dele vai repetir para sempre,
                # a não ser que a gente use um 'break' para parar.
        try: # 'try' tenta executar um código e 'except' pega erros se acontecerem.
            opcao = int(input("Qual opção deseja acessar? "))
            # 'input' pede para o usuário digitar algo.
            # 'int()' tenta transformar o que foi digitado em um número inteiro.

            if opcao == 1: # Se o usuário digitou 1...
                print("Você acessou a conta Corrente.")
            elif opcao == 2: # Se o usuário digitou 2...
                print("Você acessou a conta Poupança.")
            elif opcao == 3: # Se o usuário digitou 3...
                print("Obrigado por usar o Banco MMS. Até mais!")
                break # 'break' faz o loop 'while True' parar, encerrando o programa.
            else: # Se o usuário digitou qualquer outra coisa que não seja 1, 2 ou 3...
                print("Opção inválida. Por favor, digite 1, 2 ou 3.")
        except ValueError: # Se o que o usuário digitou NÃO PODE ser transformado em número (ex: digitou "abc")...
            print("Entrada inválida. Por favor, digite um NÚMERO (1, 2 ou 3).")

# --- Como o programa funciona quando você o executa ---

apresentacao() # Primeiro, chamamos a função 'apresentacao' para mostrar as boas-vindas e o menu.
logica_escolha() # Depois, chamamos a função 'logica_escolha' para que o usuário possa interagir.