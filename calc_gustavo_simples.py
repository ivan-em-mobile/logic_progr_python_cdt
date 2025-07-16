###@gustavo_ferreira

###MVC

#model
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"
    
def resto(a, b):
    return a % b


#view

while True:
    print("\n#### MENU ####")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Resto da divisão (%)")

    print("8. Sair")
    
    escolha = input("Escolha uma opção (1 a 8): ")

    if escolha == "8":
        print("Saindo...")
        break
    
    
#controller
    elif escolha in ["1", "2", "3", "4", "5", "6"]:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))

        if escolha == "1":
            print("Resultado da soma:", soma(a, b))
        elif escolha == "2":
            print("Resultado da subtração:", subtracao(a, b))
        elif escolha == "3":
            print("Resultado da multiplicação:", multiplicacao(a, b))
        elif escolha == "4":
            print("Resultado da divisão:", divisao(a, b))
        elif escolha == "5":
            print("Resto da divisão:", resto(a, b))
        else:
            print("Opção inválida. Tente novamente.")








