print("--- Cadastro de Produtos (Dicionário) ---\n")

# Um dicionário vazio para armazenar os produtos.
# A chave será o ID do produto e o valor será outro dicionário com os detalhes.
produtos = {}

print("Bem-vindo ao sistema de Cadastro de Produtos!")

# --- Loop Principal do Programa ---
while True:
    print("\n--- Opções ---")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Buscar produto por ID")
    print("4 - Listar todos os produtos")
    print("5 - Sair")

    opcao = input("Digite sua opção: ")

    if opcao == "1":
        # Opção 1: Adicionar produto
        produto_id = input("Digite o ID do produto: ")
        if produto_id in produtos:
            print(f"Erro: Produto com ID '{produto_id}' já existe.")
        else:
            nome_produto = input("Digite o nome do produto: ")
            preco_produto = input("Digite o preço do produto: ")
            # Adiciona um novo par chave-valor ao dicionário 'produtos'.
            # O valor é outro dicionário com as informações do produto.
            produtos[produto_id] = {"nome": nome_produto.strip(), "preco": preco_produto.strip()}
            print(f"Produto '{nome_produto.strip()}' (ID: {produto_id}) adicionado com sucesso!")

    elif opcao == "2":
        # Opção 2: Remover produto
        produto_id_remover = input("Digite o ID do produto a ser removido: ")
        if produto_id_remover in produtos:
            # Usa 'del' para remover um par chave-valor do dicionário.
            del produtos[produto_id_remover]
            print(f"Produto com ID '{produto_id_remover}' removido com sucesso!")
        else:
            print(f"Produto com ID '{produto_id_remover}' não encontrado.")

    elif opcao == "3":
        # Opção 3: Buscar produto por ID
        produto_id_buscar = input("Digite o ID do produto a ser buscado: ")
        if produto_id_buscar in produtos:
            # Acessa os detalhes do produto usando a chave (ID).
            detalhes = produtos[produto_id_buscar]
            print(f"\n--- Detalhes do Produto (ID: {produto_id_buscar}) ---")
            print(f"Nome: {detalhes['nome']}")
            print(f"Preço: R${detalhes['preco']}")
            print("---------------------------------------")
        else:
            print(f"Produto com ID '{produto_id_buscar}' não encontrado.")

    elif opcao == "4":
        # Opção 4: Listar todos os produtos
        print("\n--- Todos os Produtos Cadastrados ---")
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for id_prod, detalhes_prod in produtos.items():
                # .items() retorna pares (chave, valor) do dicionário.
                print(f"ID: {id_prod} | Nome: {detalhes_prod['nome']} | Preço: R${detalhes_prod['preco']}")
        print("-------------------------------------")

    elif opcao == "5":
        print("Saindo do Cadastro de Produtos... Volte sempre!")
        break

    else:
        print("Opção inválida. Tente novamente.")