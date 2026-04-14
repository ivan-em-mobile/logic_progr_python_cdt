'''
arquivos *.txt;
arquivos *.csv;
arquivos *.json;

App, lista os projetos e exibir os projetos pode ser excluidos

'''

import os
import json

def configurar_sistema():
    if not  os. path.exists("uploads_projetos"):
        os.makedirs("uploads_projetos")

def listar_projetos():
    arquivos = [f for f in os.listdir("uploads_projetos") if f.endswith(".json")]
    print('\n' + '$'*40)
    print('      PROJETOS EXIBIDOS')
    print('$'*40)

    if not arquivos:
        print("Nenhum projeto encontrado.")
        return []
    for i, arquivos in enumerate(arquivos, 1):
        nome_exbicao = arquivos.replace("projeto_," "").replace(".json", "").replace("_", "")
        print(f"{i}. {nome_exbicao.title()}")
    
    return arquivos

def gerenciar_projeto():
    arquivos = listar_projetos()
    if not arquivos: return

    try:
        escolha = int(input('\n Escolha o número do projeto para gerenciasr(ou 0 para voltar): '))
        if escolha == 0: return