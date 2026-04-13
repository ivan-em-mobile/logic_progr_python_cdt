'''
arquivos *.txt;
arquivos *.csv;
arquivos *.json;

App, lista os projetos e exibir os projetos pode ser excluidos

'''

import os
import json

def configurar_sistema():
    if not os. path.exists("uploads_projetos"):
        os.makedirs("uploads_projetos")

def listar_projetos():
    arquivos = [f for f in os.listdir("uploads_projetos") if f.endswith(".json")]
    print('\n' + '+'*40)
    print('      PROJETOS LISTADOS')
    print('+'*40)

    if not arquivos:
        print("Nenhum projeto encontrado.")
        return []
    for i, arquivos in enumerate(arquivos, 1):
        nome_exibicao = arquivos.replace("projeto_", "").replace(".json", "").replace("_", " ")
        print(f"{i}. {nome_exibicao.title()}")

    return arquivos

def gerenciar_projeto():
    arquivos = listar_projetos()
    if not arquivos: return

    try:
        escolha = int(input('\n Escolha o número do projeto para gerenciar(ou 0 para voltar): '))
        if escolha == 0: return

        nome_arquivo = arquivos[escolha - 1]
        caminho = f"uploads_projetos/{nome_arquivo}"

        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)   

        print(f"\n--- Nova Atualização ---")
        print(f"Aluno: {dados['aluno']}")
        print(f"Projeto: {dados['projeto']}")

        confirmar = input("\nDeseja alterar as informações deste projeto? (s/n): ").lower()
        if confirmar == 's':
            dados['aluno'] = input(f"Novo nome [{dados['aluno']}]: ") or dados['aluno']
            dados['projeto'] = input(f"Novo resumo: ") or dados['projeto']

            with open(caminho, "w", encoding="utf-8") as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
            print("\n[SUCESSO] Projeto atualizado com sucesso!")

    except (ValueError, IndexError):
        print("[ERRO] Escolha inválida. Voltando ao menu.")