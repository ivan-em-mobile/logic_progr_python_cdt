import random

# --- BANCO DE DADOS (ESTRUTURAS BÁSICAS) ---
clientes = {} # Nome: quantidade de pedidos
cardapio = {
    '1': ('Combo Classico Burger + Batata', 28.90),
    '2': ('Combo Bacon Burger + Batata', 32.90),
    '3': ('Combo Chicken Crispy + Batata', 33.90),
    '4': ('Combo Cheeseburger Duplo + Batata', 34.90),
    '5': ('Hamburguer Classico', 17.90),
    '6': ('Bacon Burger', 21.90),
    '7': ('Chicken Crispy Burger', 20.90),
    '8': ('Veggie Burger', 19.90),
    '9': ('Cheeseburger Duplo', 23.90)
}

# --- MENU PRINCIPAL ---
while True:
    print("\n" + "="*40)
    print("      HAMBURGUERIA PYTHON v3.0")
    print("="*40)
    print("1. Novo Pedido (Balcão)")
    print("2. Delivery")
    print("3. Trabalhe Conosco")
    print("0. Sair")
    print("-" * 40)
    
    opcao_menu = input("Escolha uma opção: ")

    if opcao_menu == '0':
        print("Encerrando sistema... Até logo!")
        break

    elif opcao_menu == '1' or opcao_menu == '2':
        # --- INÍCIO DA LÓGICA DE PEDIDO ---
        is_delivery = (opcao_menu == '2')
        carrinho = []
        total = 0.0
        endereco = "Consumo no Local"

        # 1. Identificação do Cliente
        nome = input("\nQual o seu nome? ").capitalize()
        if nome not in clientes:
            clientes[nome] = 0
        clientes[nome] += 1

        # Regra de Fidelidade
        if clientes[nome] == 5:
            print(f"⭐ PARABÉNS {nome.upper()}! Este é seu 5º pedido!")
        elif clientes[nome] > 10:
            print("❌ Limite de 10 pedidos por cliente atingido hoje.")
            continue

        # 2. Endereço (se for delivery)
        if is_delivery:
            print("\n--- DADOS DE ENTREGA ---")
            tipo_m = input("Casa ou Apartamento? ").lower()
            rua = input("Rua/Endereço: ")
            num = input("Número/Bloco: ")
            endereco = f"{rua}, {num} ({tipo_m.capitalize()})"

        # 3. Sugestão do Chef
        item_sugerido = random.choice(['5', '6', '7', '8', '9'])
        nome_sug, preco_sug = cardapio[item_sugerido]
        print(f"\n✨ SUGESTÃO DO CHEF: {nome_sug} por R$ {preco_sug:.2f}")
        if input("Deseja adicionar? (s/n): ").lower() == 's':
            carrinho.append((nome_sug, preco_sug, 1))
            total += preco_sug

        # 4. Escolha do Cardápio Principal
        while True:
            print("\n--- CARDÁPIO ---")
            for k, v in cardapio.items():
                print(f"{k}. {v[0]:.<35} R$ {v[1]:.2f}")
            
            escolha = input("\nDigite o número do item (ou 'f' para fechar carrinho): ")
            if escolha.lower() == 'f':
                break
            
            if escolha in cardapio:
                while True:
                    try:
                        qtd = int(input(f"Quantidade de {cardapio[escolha][0]}: "))
                        if qtd > 0: break
                        else: print("Quantidade deve ser maior que zero.")
                    except ValueError:
                        print("Por favor, digite apenas números.")
                
                carrinho.append((cardapio[escolha][0], cardapio[escolha][1], qtd))
                total += (cardapio[escolha][1] * qtd)
                
                # Checar se é um COMBO (itens 1 a 4) para a bebida grátis
                tem_combo = False
                for item in carrinho:
                    # Verifica se o nome do item no carrinho é um dos nomes dos combos
                    for i in range(1, 5):
                        if item[0] == cardapio[str(i)][0]:
                            tem_combo = True
            else:
                print("❌ Opção inválida!")

        if not carrinho:
            print("Carrinho vazio. Retornando...")
            continue

        # 5. Bebida
        bebida_nome = "Sem bebida"
        bebida_preco = 0.0
        add_bebida = 'n'
        
        if tem_combo:
            print("\n🎁 COMBO DETECTADO! Você ganhou uma bebida grátis.")
            add_bebida = 's'
        else:
            add_bebida = input("\nDeseja adicionar bebida? (s/n): ").lower()

        if add_bebida == 's':
            print("1. Suco (R$ 9.00) | 2. Refrigerante (R$ 7.00)")
            tipo_b = input("Escolha: ")
            if tipo_b == '1':
                bebida_nome = "Suco de Laranja"
                bebida_preco = 0.0 if tem_combo else 9.0
            else:
                bebida_nome = "Coca-Cola"
                bebida_preco = 0.0 if tem_combo else 7.0
            total += bebida_preco

        # 6. Taxa de Entrega
        taxa_entrega = 0.0
        if is_delivery:
            if total >= 60:
                print("\n✨ PEDIDO ACIMA DE R$60: FRETE GRÁTIS!")
            else:
                taxa_entrega = 10.0
                total += taxa_entrega

        # 7. Pagamento
        print("\nPagamento: 1. Dinheiro | 2. Cartão | 3. Pix")
        pg_op = input("Escolha: ")
        pagamento = "Dinheiro" if pg_op == '1' else ("Cartão" if pg_op == '2' else "Pix")

        # --- RECIBO FINAL ---
        print("\n" + "="*45)
        print(f"{'RESUMO DO PEDIDO':^45}")
        print("="*45)
        print(f"Cliente: {nome} | Pedido: #{random.randint(1000,9999)}")
        print(f"Endereço: {endereco}")
        print("-" * 45)
        for item in carrinho:
            print(f"{item[2]}x {item[0]:.<30} R$ {item[1]*item[2]:.2f}")
        if bebida_nome != "Sem bebida":
            print(f"1x {bebida_nome:.<30} R$ {bebida_preco:.2f}")
        if taxa_entrega > 0:
            print(f"Taxa de Entrega: {'.':.<17} R$ {taxa_entrega:.2f}")
        
        print("-" * 45)
        print(f"TOTAL A PAGAR: {'.':.<19} R$ {total:.2f}")
        print(f"Forma de Pagamento: {pagamento}")
        print(f"Tempo Estimado: {random.randint(25,45)} min")
        print("="*45)

    elif opcao_menu == '3':
        # --- LÓGICA DE RH (VAGAS) ---
        vagas = {
            '1': ('Cozinheiro', 25, 5),
            '2': ('Atendente', 17, 1),
            '3': ('Chapeiro', 21, 2)
        }
        print("\nVAGAS DISPONÍVEIS:")
        for k, v in vagas.items():
            print(f"{k}. {v[0]}")
        
        v_esc = input("Selecione a vaga: ")
        if v_esc in vagas:
            try:
                idade = int(input("Sua idade: "))
                exp = int(input("Anos de experiência: "))
                v_nome, v_idade, v_exp = vagas[v_esc]
                
                if idade >= v_idade and exp >= v_exp:
                    print(f"✅ Candidato para {v_nome} aprovado para entrevista!")
                else:
                    print("❌ Requisitos mínimos não atingidos.")
            except ValueError:
                print("❌ Erro: Digite números para idade e experiência.")
        else:
            print("Vaga inválida.")

    else:
        print("❌ Opção Inválida. Tente novamente.")