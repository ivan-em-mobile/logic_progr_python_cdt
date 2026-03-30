# MÓDULO DE MANIPULAÇÃO DE ARQUIVOS EM PYTHON

# -----------------------------------------------
# FUNÇÃO 1: Obter Dados do Filme do Usuário (Leitura de Entrada)
# -----------------------------------------------
def obter_dados_do_usuario_txt():
    """
    Solicita ao usuário as informações necessárias para cadastrar um filme com validação.
    Retorna os dados como uma tupla (ano, titulo, tema, sinopse) ou None se falhar.
    """
    print("\n--- Cadastro de Novo Filme ---")
    ano = input("Digite o ano do filme (4 dígitos): ").strip()
    titulo = input("Digite o título do filme: ").strip()
    tema = input("Digite o tema/gênero do filme: ").strip()
    sinopse = input("Digite uma sinopse curta: ").strip()
    
    # Validação de Ano: deve ser um número e ter 4 dígitos
    if not ano.isdigit() or len(ano) != 4:
        print("🚨 Erro: O ano deve ser um número de 4 dígitos. Filme não salvo.")
        return None
    
    # Validação dos demais campos
    if not all([titulo, tema, sinopse]):
        print("🚨 Erro: Título, tema e sinopse são obrigatórios. Filme não salvo.")
        return None
        
    return (ano, titulo, tema, sinopse)

# -----------------------------------------------
# Documentação Solicitada sobre Escrita
# -----------------------------------------------
'''
Função para Adicionar um Novo Filme;
Usa o gerenciador de contexto para abrir o 
arquivo no modo 'a' (Append);
O modo 'a' garante que o novo filme seja adicionado ao final,
sem apagar o conteúdo existente.
'''
# -----------------------------------------------
# FUNÇÃO 2: Adicionar um Novo Filme (Escrita em TXT - Modo 'a')
# -----------------------------------------------
def adicionar_filme(ano, titulo, tema, sinopse):
    """
    Adiciona um novo filme ao final do arquivo 'catalogo_filmes.txt'.
    Usa o modo 'a' (Append) para inserção.
    """
    nome_arquivo = "catalogo_filmes.txt"
    # Formato: ano;titulo;tema;sinopse\n
    nova_linha = f"{ano};{titulo};{tema};{sinopse}\n"

    try:
        # Usa o modo 'a' (Append) para adicionar no final
        with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write(nova_linha)
        print(f"\n✅ Filme '{titulo}' adicionado ao catálogo com sucesso!")

    except Exception as e:
        print(f"\n❌ Ocorreu um erro ao salvar o filme: {e}")

# -----------------------------------------------
# FUNÇÃO 3: Fluxo de Escrita (Combina obter dados + adicionar)
# -----------------------------------------------
def escrever_novo_filme():
    """
    Controla o fluxo completo para cadastrar um novo filme.
    """
    dados_novo_filme = obter_dados_do_usuario_txt()
    
    if dados_novo_filme:
        # Desempacota a tupla de dados em argumentos separados
        adicionar_filme(*dados_novo_filme)

# -----------------------------------------------
# FUNÇÃO 4: Exibir Catálogo (Leitura do TXT - Modo 'r')
# -----------------------------------------------
def exibir_catalogo_txt():
    """
    Lê o arquivo 'catalogo_filmes.txt', separa os dados e exibe formatado.
    """
    nome_arquivo = "catalogo_filmes.txt"
    print("\n==============================================")
    print("🎬 CATÁLOGO DE FILMES ATUALIZADO 🎬")
    print("==============================================")
    
    filmes_encontrados = False
    
    try:
        # Abre o arquivo no modo 'r' (Read - Leitura)
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            print(f"{'ANO':<5} | {'TÍTULO':<30} | {'TEMA':<20}")
            print("-" * 75)
            
            for linha in arquivo:
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue 
                    
                dados = linha_limpa.split(';')
                
                if len(dados) == 4:
                    ano, titulo, tema, sinopse = dados
                    filmes_encontrados = True
                    
                    print(f"**{ano:<5}** | **{titulo:<30}** | {tema:<20}")
                    print(f"        -> Sinopse: {sinopse.strip()}")
                    print("-" * 75)
            
            if filmes_encontrados:
                print("==============================================")

    except FileNotFoundError:
        print("⚠️ O Catálogo está vazio. Nenhum arquivo encontrado. Comece a cadastrar!")
        print("==============================================")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado durante a leitura: {e}")

# -----------------------------------------------
# FUNÇÃO 5: Pesquisar Filmes por Ano (Leitura e Filtragem)
# -----------------------------------------------
def pesquisar_filme_por_ano():
    """
    Pede ao usuário um ano e exibe apenas os filmes lançados naquele ano.
    """
    nome_arquivo = "catalogo_filmes.txt"
    
    ano_busca = input("\n🔍 Digite o ANO que deseja buscar (4 dígitos): ").strip()
    
    if not ano_busca.isdigit() or len(ano_busca) != 4:
        print("🚨 Erro: O ano de busca deve ser um número de 4 dígitos.")
        return
        
    filmes_encontrados = 0

    print("\n==============================================")
    print(f"🔎 RESULTADOS PARA O ANO: {ano_busca}")
    print("==============================================")

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            print(f"{'ANO':<5} | {'TÍTULO':<30} | {'TEMA':<20}")
            print("-" * 75)
            
            for linha in arquivo:
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue
                    
                dados = linha_limpa.split(';')
                
                if len(dados) == 4:
                    ano, titulo, tema, sinopse = dados
                    
                    # LÓGICA DE FILTRAGEM
                    if ano.strip() == ano_busca:
                        print(f"**{ano:<5}** | **{titulo:<30}** | {tema:<20}")
                        print(f"        -> Sinopse: {sinopse.strip()}")
                        print("-" * 75)
                        filmes_encontrados += 1
                        
            if filmes_encontrados == 0:
                print(f"Nenhum filme encontrado para o ano '{ano_busca}'.")
                
        print("==============================================")

    except FileNotFoundError:
        print("⚠️ Catálogo não encontrado. Adicione filmes primeiro!")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

# -----------------------------------------------
# FUNÇÃO 6: Alterar Filme (Leitura + Reescrita - Modo 'r' e 'w')
# -----------------------------------------------
def alterar_filme():
    """
    Permite ao usuário buscar um filme pelo título e alterar a sinopse.
    Requer a leitura e reescrita completa do arquivo ('r' seguido por 'w').
    """
    nome_arquivo = "catalogo_filmes.txt"
    filmes_modificados = []
    encontrado = False

    titulo_busca = input("\n📝 Digite o TÍTULO do filme que deseja alterar: ").strip()
    
    try:
        # 1. LER todo o arquivo ('r')
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha_limpa = linha.strip()
                if not linha_limpa:
                    continue
                
                dados = linha_limpa.split(';')
                
                if len(dados) == 4:
                    ano, titulo, tema, sinopse = dados
                    
                    # 2. VERIFICAR e MODIFICAR na memória
                    if titulo.strip().lower() == titulo_busca.lower():
                        encontrado = True
                        print(f"\nFilme encontrado: **{titulo}** (Ano: {ano})")
                        
                        nova_sinopse = input("Digite a NOVA Sinopse para este filme: ").strip()
                        
                        if nova_sinopse:
                            sinopse = nova_sinopse
                            print("✅ Sinopse atualizada na memória!")
                        else:
                            print("⚠️ Sinopse mantida.")

                    # 3. Adicionar a linha (modificada ou original) à lista
                    nova_linha = f"{ano};{titulo};{tema};{sinopse}\n"
                    filmes_modificados.append(nova_linha)
                
        if not encontrado:
            print(f"\n❌ Filme com título '{titulo_busca}' não encontrado no catálogo.")
            return

        # 4. REESCREVER o arquivo inteiro ('w')
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(filmes_modificados)
        
        print(f"\n💾 Arquivo '{nome_arquivo}' reescrito com as alterações. O catálogo foi atualizado.")

    except FileNotFoundError:
        print("⚠️ Catálogo não encontrado. Adicione filmes primeiro!")
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")

# -----------------------------------------------
# EXECUÇÃO PRINCIPAL (Fluxo Sequencial Sem Menu)
# -----------------------------------------------
if __name__ == "__main__":
    
    print("--- INÍCIO DO PROGRAMA: Catálogo de Filmes ---")
    
    # AÇÃO 1: Cadastrar um Novo Filme
    print("\n[AÇÃO 1: CADASTRO DE NOVO FILME]")
    escrever_novo_filme()
    
    # AÇÃO 2: Exibir o Catálogo Completo
    print("\n[AÇÃO 2: EXIBIÇÃO DO CATÁLOGO]")
    exibir_catalogo_txt()
    
    # AÇÃO 3: Pergunta se o usuário deseja Pesquisar por Ano (Opcional)
    print("\n[AÇÃO 3: PESQUISA OPCIONAL]")
    fazer_pesquisa = input("Deseja realizar uma pesquisa de filmes por ANO agora? (s/n): ").strip().lower()
    
    if fazer_pesquisa == 's':
        pesquisar_filme_por_ano()
        
    print("\n--- PROGRAMA FINALIZADO ---")