

# 🍔 Sistema de Gerenciamento - Hamburgueria

Este é um projeto desenvolvido em **Python** com o objetivo de simular o funcionamento de uma hamburgueria, permitindo que clientes façam pedidos, escolham delivery, e até se candidatem a vagas de emprego.

O sistema utiliza estruturas fundamentais da linguagem para organizar pedidos, cardápio, pagamentos e cadastro de clientes.

## 🚀 Funcionalidades

O sistema é dividido em módulos principais:

1. **🍟 Cardápio Interativo:**

   * Combos e lanches individuais com preços.
   * Destaque para itens especiais (🥇🥈🥉).
   * Escolha de quantidade e cálculo automático de subtotal.

2. **⭐ Sugestão do Chef:**

   * Geração aleatória de um lanche usando `random`.
   * Opção de adicionar ao pedido.

3. **🥤 Seleção de Bebidas:**

   * Escolha entre sucos e refrigerantes.
   * Integração automática com combos (bebida inclusa).

4. **🍗 Acompanhamentos:**

   * Adição opcional de itens extras como nuggets, batata e molhos.
   * Seleção múltipla com validação.

5. **💳 Sistema de Pagamento:**

   * Opções: Dinheiro, Cartão (Crédito/Débito) e Pix.
   * Validação de escolha do usuário.

6. **🚚 Delivery:**

   * Cadastro de endereço para casa ou apartamento.
   * Cálculo de taxa de entrega:

     * **Grátis** para pedidos acima de R$60
     * Taxa fixa de R$10 para valores menores

7. **👤 Histórico de Clientes:**

   * Registro simples de clientes.
   * Contador de pedidos realizados.

8. **📦 Resumo do Pedido:**

   * Número do pedido gerado aleatoriamente.
   * Tempo estimado de entrega/preparo.
   * Exibição detalhada dos itens, pagamento e total.

9. **💼 Trabalhe Conosco:**

   * Lista de vagas disponíveis.
   * Validação de idade mínima e experiência.
   * Aprovação automática baseada nos requisitos.

---

## 🛠️ Tecnologias e Estruturas Utilizadas

O projeto foi construído utilizando conceitos fundamentais de Python:

* **Dicionários (`{}`):**

  * Armazenamento de combos, lanches, bebidas, clientes e vagas.

* **Listas (`[]`):**

  * Carrinho de compras e itens do pedido.

* **Tuplas (`()`):**

  * Representação de produtos (nome e preço).

* **Laços de Repetição (`while`):**

  * Menu principal e navegação do sistema.

* **Condicionais (`if/elif/else`):**

  * Controle de fluxo e validação de entradas.

* **Tratamento de Erros (`try/except`):**

  * Validação de entradas numéricas.

* **Biblioteca `random`:**

  * Sugestão do chef.
  * Número do pedido e tempo estimado.

---

## 📋 Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Salve o arquivo como, por exemplo:
   `hamburgueria.py`
3. Abra o terminal ou prompt de comando.
4. Execute o comando:

```bash
python hamburgueria.py
```

---

## 📌 Observações

* O sistema é totalmente interativo via terminal.
* Ideal para prática de lógica de programação e estruturas de dados.
* Pode ser expandido futuramente com:

  * Interface gráfica (GUI)
  * Banco de dados
  * Sistema de login completo

---

