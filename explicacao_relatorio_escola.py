# Lista global para armazenar os dados (Conceito de Listas da apostila)
turma = []

def adicionar_aluno():
    """Captura nome e nota e guarda na lista como um dicionário."""
    nome = input("Nome do aluno: ")
    try:
        nota = float(input(f"Nota de {nome}: "))
        # Guardamos como um dicionário dentro da lista
        aluno = {"nome": nome, "nota": nota}
        turma.append(aluno)
        print(f"Aluno {nome} adicionado com sucesso!")
    except ValueError:
        print("[ERRO] Digite um número válido para a nota.")

def exibir_relatorio():
    """Percorre a lista e mostra quem passou ou reprovou."""
    print("\n--- RELATÓRIO DA TURMA ---")
    if not turma:
        print("Nenhum aluno registado.")
        return

    soma_notas = 0
    for aluno in turma:
        status = "APROVADO" if aluno['nota'] >= 7.0 else "REPROVADO"
        print(f"Nome: {aluno['nome']} | Nota: {aluno['nota']} | Status: {status}")
        soma_notas += aluno['nota']
    
    media = soma_notas / len(turma)
    print(f"--------------------------")
    print(f"Média Geral da Turma: {media:.2f}")

def menu_escolar():
    """Menu principal seguindo a estrutura de repetição while."""
    while True:
        print("\n1. Adicionar Aluno")
        print("2. Exibir Relatório")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            exibir_relatorio()
        elif opcao == "0":
            print("Saindo do sistema escolar...")
            break
        else:
            print("Opção inválida!")

# Execução
menu_escolar()