import json
from pathlib import Path

# Configuração inicial
PASTA_PROJETOS = Path("uploads_projetos")
PASTA_PROJETOS.mkdir(exist_ok=True)

def salvar_projeto(dados):
    nome_arq = f"projeto_{dados['aluno'].lower().replace(' ', '_')}.json"
    caminho = PASTA_PROJETOS / nome_arq
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def listar_e_escolher():
    arquivos = list(PASTA_PROJETOS.glob("*.json"))
    if not arquivos:
        print("\n[!] Nenhum projeto encontrado.")
        return None
    
    print("\n--- PROJETOS ---")
    for i, arq in enumerate(arquivos, 1):
        nome = arq.stem.replace("projeto_", "").replace("_", " ").title()
        print(f"{i}. {nome}")
    
    try:
        escolha = int(input("\nEscolha o número (ou 0 para voltar): "))
        return arquivos[escolha - 1] if escolha > 0 else None
    except (ValueError, IndexError):
        return None

def menu():
    while True:
        print("\n" + "-"*30 + "\n  SISTEMA SIMPLIFICADO 3.1\n" + "-"*30)
        opcao = input("1. Novo Projeto\n2. Gerenciar\n0. Sair\n> ")

        if opcao == "1":
            aluno = input("Nome do aluno: ")
            resumo = input("Resumo: ")
            salvar_projeto({"aluno": aluno, "projeto": resumo})
            print("[SUCESSO] Salvo.")

        elif opcao == "2":
            arquivo = listar_e_escolher()
            if arquivo:
                with open(arquivo, "r", encoding="utf-8") as f:
                    dados = json.load(f)
                print(f"\nAtual: {dados['aluno']} - {dados['projeto']}")
                
                if input("Alterar? (s/n): ").lower() == 's':
                    dados['aluno'] = input(f"Novo nome [{dados['aluno']}]: ") or dados['aluno']
                    dados['projeto'] = input("Novo resumo: ") or dados['projeto']
                    salvar_projeto(dados)

        elif opcao == "0": break

if __name__ == "__main__":
    menu()