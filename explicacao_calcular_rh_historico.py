import json  # Biblioteca para lidar com ficheiros JSON
import os    # Biblioteca para verificar se o ficheiro existe

NOME_ARQUIVO = "historico_bonus.json"

# 1. Função de Cálculo (Módulo 6)
def calcular_bonus(salario, anos_servico):
    porcentagem = 0.20 if anos_servico >= 5 else 0.10
    return salario * porcentagem

# 2. Função para SALVAR no ficheiro (Persistência)
def salvar_dados(lista_historico):
    with open(NOME_ARQUIVO, "w", encoding="utf-8") as f:
        # indent=4 deixa o ficheiro fácil de ler para humanos
        json.dump(lista_historico, f, indent=4, ensure_ascii=False)
    print("\n[OK] Dados salvos com sucesso!")

# 3. Função para LER do ficheiro
def carregar_dados():
    if os.path.exists(NOME_ARQUIVO):
        with open(NOME_ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return [] # Retorna lista vazia se o ficheiro não existir

# --- PROGRAMA PRINCIPAL ---

historico = carregar_dados()

while True:
    print("\n=== Gestão de Bónus ===")
    print("1. Calcular Novo Bónus")
    print("2. Ver Histórico Salvo")
    print("3. Gravar e Sair")
    
    opcao = input("\nEscolha: ")

    if opcao == "1":
        nome = input("Nome do funcionário: ")
        salario = float(input("Salário (R$): "))
        anos = int(input("Anos de casa: "))
        
        valor_bonus = calcular_bonus(salario, anos)
        
        # Criamos um registo (Dicionário)
        registo = {
            "nome": nome,
            "salario_base": salario,
            "bonus": valor_bonus,
            "total": salario + valor_bonus
        }
        
        historico.append(registo)
        print(f"\n>> Bónus de {nome}: R$ {valor_bonus:.2f}")

    elif opcao == "2":
        print("\n--- HISTÓRICO CARREGADO ---")
        if not historico:
            print("Nenhum dado encontrado.")
        for item in historico:
            print(f"Func.: {item['nome']} | Bónus: R$ {item['bonus']:.2f}")

    elif opcao == "3":
        salvar_dados(historico)
        print("Encerrando sistema...")
        break