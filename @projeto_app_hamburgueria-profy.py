import random
import os

# --- BANCO DE DADOS INTEGRADO ---
clientes = {}

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

acompanhamentos = {
    '1': ('Nuggets', 9.00),
    '2': ('Batata extra', 7.00),
    '3': ('Onion Rings', 8.00),
    '4': ('Molho Barbecue', 4.00),
    '5': ('Molho Alho', 4.00),
    '6': ('Molho Especial', 5.00)
}

bebidas = {
    'sucos': {'1': ('Suco de Laranja', 9.0), '2': ('Suco de Morango', 9.0), '3': ('Suco de Maracuja', 9.0)},
    'refris': {'1': ('Coca Cola', 7.0), '2': ('Guarana', 7.0), '3': ('Fanta', 7.0)}
}

vagas = {
    '1': ('Cozinheiro', 25, 5),
    '2': ('Atendente', 17, 1),
    '3': ('Chapeiro', 21, 2),
    '4': ('Entregador', 18, 0),
    '5': ('Gerente', 30, 5),
    '6': ('Auxiliar de Cozinha', 18, 0),
    '7': ('Caixa', 18, 1)
}

# --- FUNÇÕES DE APOIO ---

def formatar(valor):
    return f"R$ {valor:.2f}"

def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("❌ Erro: Digite apenas números.")

def selecionar_bebida(gratis=False):
    print(f"\n--- BEBIDAS {'(CORTESIA)' if gratis else ''} ---")
    tipo = input("1. Suco | 2. Refrigerante: ")
    cat = 'sucos' if tipo == '1' else 'refris'
    
    for k, v in bebidas[cat].items():
        print(f"{k}. {v[0]} {' ' if gratis else formatar(v[1])}")
    
    esc = input("Escolha o sabor: ")
    item = bebidas[cat].get(esc, ("Bebida Padrão", 7.0))
    return item[0], (0 if gratis else item[1])

# --- LÓGICA PRINCIPAL ---

def fazer_pedido(delivery=False):
    # 1. Identificação e Fidelidade
    nome = input("\nNome do cliente: ").capitalize()
    if nome not in clientes:
        clientes[nome] = {"pedidos": 0}
    
    clientes[nome]["pedidos"] += 1
    num_p = clientes[nome]["pedidos"]

    if num_p == 5:
        print("\n🎉 PARABÉNS! Você completou 5 pedidos conosco! Ganhou um selo de fidelidade.")
    elif num_p > 10:
        print("❌ Limite de pedidos diários atingido para este cliente.")
        return

    # 2. Endereço se for Delivery
    endereco = "Consumo no Local"
    if delivery:
        tipo = input("Casa ou Apartamento? ").lower()
        rua = input("Endereço: ")
        detalhe = input("Número/Bloco: ")
        endereco = f"{rua}, {detalhe} ({tipo.capitalize()})"

    carrinho = []
    
    # 3. Sugestão do Chef
    sugestao = cardapio[random.choice(['5', '6', '7', '8', '9'])]
    print(f"\n⭐ SUGESTÃO DO CHEF: {sugestao[0]} por {formatar(sugestao[1])}")
    if input("Deseja adicionar? (s/n): ").lower() == 's':
        carrinho.append({'nome': sugestao[0], 'preco': sugestao[1], 'qtd': 1, 'id': 'chef'})

    # 4. Escolha do Cardápio
    while True:
        print("\n--- CARDÁPIO ---")
        for k, v in cardapio.items():
            tag = "🥇" if k == '3' else ("🥈" if k == '5' else ("🥉" if k == '9' else ""))
            print(f"{k}. {v[0]:.<35} {formatar(v[1])} {tag}")
        
        esc = input("\nItem (ou 'f' para finalizar): ")
        if esc.lower() == 'f': break
        
        if esc in cardapio:
            qtd = input_int(f"Quantidade de {cardapio[esc][0]}: ")
            if qtd > 0:
                carrinho.append({'nome': cardapio[esc][0], 'preco': cardapio[esc][1], 'qtd': qtd, 'id': esc})
        else:
            print("Opção inválida!")

    if not carrinho: return

    # 5. Acompanhamentos
    extras = []
    if input("\nDeseja acompanhamentos? (s/n): ").lower() == 's':
        for k, v in acompanhamentos.items():
            print(f"{k}. {v[0]:.<20} {formatar(v[1])}")
        while True:
            ac = input("Escolha (0 para parar): ")
            if ac == '0': break
            if ac in acompanhamentos: extras.append(acompanhamentos[ac])

    # 6. Bebida e Regra de Combo
    # Se ID entre 1 e 4 (Combos), bebida é grátis
    tem_combo = any(i['id'].isdigit() and 1 <= int(i['id']) <= 4 for i in carrinho)
    
    bebida_n, bebida_p = "Sem bebida", 0
    if tem_combo:
        print("\n🎁 Seu combo dá direito a uma bebida grátis!")
        bebida_n, bebida_p = selecionar_bebida(gratis=True)
    elif input("\nDeseja bebida? (s/n): ").lower() == 's':
        bebida_n, bebida_p = selecionar_bebida(gratis=False)

    # 7. Pagamento e Taxas
    subtotal = sum(i['preco'] * i['qtd'] for i in carrinho) + sum(e[1] for e in extras) + bebida_p
    taxa = 10.0 if delivery and subtotal < 60 else 0.0
    
    print("\nPagamento: 1.Dinheiro | 2.Cartão | 3.Pix")
    metodo = {"1":"Dinheiro", "2":"Cartão", "3":"Pix"}.get(input("Escolha: "), "Dinheiro")

    # --- RECIBO FINAL ---
    print("\n" + "="*50)
    print(f"{'HAMBURGUERIA PYTHON - RECIBO':^50}")
    print("="*50)
    print(f"Cliente: {nome} | Pedido: #{random.randint(1000,9999)}")
    print(f"Endereço: {endereco}")
    print("-" * 50)
    for i in carrinho:
        print(f"{i['qtd']}x {i['nome']:.<35} {formatar(i['preco']*i['qtd'])}")
    for e in extras:
        print(f"1x {e[0]:.<35} {formatar(e[1])}")
    if bebida_n != "Sem bebida":
        print(f"1x {bebida_n:.<35} {formatar(bebida_p)}")
    
    if taxa > 0: print(f"Taxa de Entrega: {formatar(taxa)}")
    elif delivery: print("✨ FRETE GRÁTIS (Pedido acima de R$60)!")
    
    print("-" * 50)
    print(f"{'TOTAL:':<38} {formatar(subtotal + taxa)}")
    print(f"Forma de Pagamento: {metodo}")
    print(f"Tempo Estimado: {random.randint(20,40)} min")
    print("="*50)

# --- MENU PRINCIPAL ---

while True:
    print("\n🍔 SISTEMA DE GESTÃO - HAMBURGUERIA")
    print("1. Novo Pedido (Balcão)")
    print("2. Delivery")
    print("3. Trabalhe Conosco (Vagas)")
    print("0. Sair")
    
    op = input("Opção: ")
    
    if op == '1': fazer_pedido(delivery=False)
    elif op == '2': fazer_pedido(delivery=True)
    elif op == '3':
        print("\nVAGAS:")
        for k, v in vagas.items(): print(f"{k}. {v[0]}")
        esc = input("Vaga desejada: ")
        if esc in vagas:
            idade = input_int("Idade: ")
            exp = input_int("Anos de experiência: ")
            v_nome, min_id, min_ex = vagas[esc]
            if idade >= min_id and exp >= min_ex:
                print(f"✅ Perfil aprovado para {v_nome}!")
            else:
                print("❌ Não atende aos requisitos mínimos.")
    elif op == '0':
        print("Encerrando... Obrigado por usar o sistema!")
        break