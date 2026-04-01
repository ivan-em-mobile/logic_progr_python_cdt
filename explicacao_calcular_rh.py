# 1. DEFINIÇÃO DA FUNÇÃO (Pág. 31 da apostila)
def calcular_bonus(salario, anos_servico):
    """
    Calcula o bónus baseado no tempo de casa.
    Retorna o valor em dinheiro do bónus.
    """
    if anos_servico >= 5:
        porcentagem = 0.20  # 20%
    else:
        porcentagem = 0.10  # 10%
    
    valor_do_bonus = salario * porcentagem
    
    # 2. RETORNO (Pág. 32 da apostila)
    return valor_do_bonus

# --- PROGRAMA PRINCIPAL ---

print("=== Sistema de Bónus de Funcionários ===")

# Entrada de dados
s = float(input("Digite o salário atual (R$): "))
t = int(input("Digite quantos anos trabalha na empresa: "))

# 3. CHAMADA DA FUNÇÃO (Pág. 33 da apostila)
# Passamos 's' e 't' como argumentos para a função
bonus_recebido = calcular_bonus(s, t)

# Cálculo do total
total_com_bonus = s + bonus_recebido

print(f"\n--- Resultado ---")
print(f"O seu bónus é de: R$ {bonus_recebido:.2f}")
print(f"O seu novo salário será: R$ {total_com_bonus:.2f}")