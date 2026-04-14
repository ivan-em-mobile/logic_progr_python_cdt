# 1. Definição da função com parâmetros (pág. 31)
def converter_moeda(valor_reais, taxa_cambio):
    """
    Função que calcula a conversão de moeda.
    valor_reais: float
    taxa_cambio: float
    return: valor convertido
    """
    valor_convertido = valor_reais / taxa_cambio
    
    # 2. Uso do RETURN (pág. 32)
    # O return "entrega" o resultado para quem chamou a função
    return valor_convertido

# --- Programa Principal ---

print("=== Sistema de Câmbio ===")
valor = float(input("Quanto dinheiro tem em Reais (R$)? "))
taxa = float(input("Qual a cotação atual do Dólar? "))

# 3. Chamada da função guardando o resultado numa variável
resultado = converter_moeda(valor, taxa)

print(f"\nCom R${valor:.2f}, você pode comprar ${resultado:.2f} dólares.")