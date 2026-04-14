import os

def configurar_sistema():
    """Cria a pasta de uploads caso ela não exista."""
    if not os.path.exists("uploads_projetos"):
        os.makedirs("uploads_projetos")
        print(">> Pasta 'uploads_projetos' criada com sucesso.")

def fazer_upload():
    """Simula o upload de um arquivo de texto."""
    print('\n' + '='*40)
    print('  Sistema de upload dos arquivos jovens  ')
    print('='*40)

    nome_aluno = input("Digite o nome do aluno: ").strip().replace(" ", "_")
    conteudo = input("Cole aqui o resumo do seu projeto: ")

    # Definimos o caminho do arquivo dentro da pasta
    caminho_arquivo = f"uploads_projetos/projeto_{nome_aluno}.txt"

    # Criamos o arquivo (Simulando o Upload)
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Projeto enviado por: {nome_aluno}\n")
        arquivo.write("-" * 30 + "\n")
        arquivo.write(conteudo)

    print(f"\n[SUCESSO] Arquivo 'projeto_{nome_aluno}.txt' enviado para a pasta!")

# --- Execução ---
configurar_sistema()
fazer_upload()