'''
Função para Inserir Dados e Escrever no Catálogo

OBJETIVO:
1. LEITURA DE ENTRADA: Capturar os dados do novo filme diretamente do usuário (ano, título, tema, sinopse).
2. ESCRITA NO ARQUIVO: Persistir (salvar) esses dados no arquivo 'catalogo_filmes.txt'.

MODO DE OPERAÇÃO (ESCRITA):
- Utiliza o gerenciador de contexto `with open(...)` no modo **'a' (Append)**. 
- O modo 'a' garante que o novo filme seja **adicionado ao final** do arquivo, sem apagar o conteúdo existente.
'''
def obter_dados_do_usuario_txt():
    """
    Solicita ao usuário as informações necessárias para cadastrar um filme.
    Retorna os dados como uma tupla (ano, titulo, tema, sinopse).
    """
    print("\n--- Cadastro de Novo Filme ---")
    ano = input("Digite o ano do filme: ").strip()
    titulo = input("Digite o título do filme: ").strip()
    tema = input("Digite o tema/gênero do filme: ").strip()
    sinopse = input("Digite uma sinopse curta: ").strip()
    
    # Validação simples
    if not all([ano, titulo, tema, sinopse]):
        print("🚨 Erro: Todos os campos são obrigatórios. O filme não será salvo.")
        return None
        
    return (ano, titulo, tema, sinopse)

def adicionar_filme(ano, titulo, tema, sinopse):
    """
    Adiciona um novo filme ao final do arquivo 'catalogo_filmes.txt'.
    Cada campo é separado por ponto e vírgula (;).
    """
    nome_arquivo = "catalogo_filmes.txt"
    # Formato: ano;titulo;tema;sinopse\n
    nova_linha = f"{ano};{titulo};{tema};{sinopse}\n"

    try:
        # Usa o modo 'a' (Append) para adicionar no final, sem apagar o conteúdo anterior
        with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write(nova_linha)
        print(f"\n✅ Filme '{titulo}' adicionado ao catálogo com sucesso!")

    except Exception as e:
        print(f"\n❌ Ocorreu um erro ao salvar o filme: {e}")

def exibir_catalogo_txt():
    """
    Lê o arquivo 'catalogo_filmes.txt', separa os dados e exibe formatado.
    A sinopse é exibida em uma linha separada para manter a organização.
    """
    nome_arquivo = "catalogo_filmes.txt"

    print("\n==============================================")
    print("🎬 CATÁLOGO DE FILMES ATUALIZADO 🎬")
    print("==============================================")
    
    filmes_encontrados = False # Variável de controle
    
    try:
        # Abre o arquivo no modo 'r' (Read - Leitura)
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            
            # Cabeçalho Fixo
            print(f"{'ANO':<5} | {'TÍTULO':<30} | {'TEMA':<20}")
            print("-" * 75)
            
            linhas = arquivo.readlines()

            for linha in linhas:
                dados = linha.strip().split(';')
                
                # Processa e exibe a linha se ela estiver completa
                if len(dados) == 4:
                    ano, titulo, tema, sinopse = dados
                    filmes_encontrados = True
                    
                    # 1. Exibe a linha principal (Ano, Título, Tema)
                    print(f"**{ano:<5}** | **{titulo:<30}** | {tema:<20}")
                    
                    # 2. Exibe a Sinopse em uma linha abaixo com recuo
                    print(f"        -> Sinopse: {sinopse.strip()}")
                    print("-" * 75) # Separador visual para cada filme
            
            # Se encontrou filmes, garante que o rodapé seja impresso
            if filmes_encontrados:
                print("==============================================")


    except FileNotFoundError:
        print("⚠️ O Catálogo está vazio. Nenhum arquivo encontrado. Comece a cadastrar!")
        print("==============================================")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado durante a leitura: {e}")

if __name__ == "__main__":
    
    print("--- INÍCIO DO PROGRAMA ---")
    
    # 1. Pede os dados ao usuário
    dados_novo_filme = obter_dados_do_usuario_txt()
    
    # 2. Se os dados forem válidos (não None), salva o filme
    if dados_novo_filme:
        # O *dados_novo_filme desempacota a tupla em 4 argumentos separados
        adicionar_filme(*dados_novo_filme)
        
    # 3. Exibe o catálogo atualizado para o usuário!
    exibir_catalogo_txt()
    
    print("\n--- PROGRAMA FINALIZADO ---")