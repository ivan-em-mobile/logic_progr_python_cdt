'''
calculo_notas.py

Documentação: Função para calcular a média das notas
Esta função recebe uma lista de notas e retorna a média aritmética.
Parâmetros:
- notas (list): Uma lista contendo os valores das notas (números float ou int).
Retorno:
- float: O valor da média calculada.

'''


def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas."""
    # A função sum() soma todos os elementos da lista.
    soma_das_notas = sum(notas)
    # len() retorna o número de elementos na lista.
    numero_de_notas = len(notas)
    
    # Evita divisão por zero caso a lista de notas esteja vazia.
    if numero_de_notas == 0:
        return 0.0
    
    media = soma_das_notas / numero_de_notas
    return media

## 2. Lógica Principal do Programa
def sistema_calculo_notas():
    print("--- Sistema de Cálculo de Notas ---")
    
    # Lista para armazenar as notas digitadas pelo usuário.
    notas_do_aluno = []
    
    # Loop para solicitar as 3 notas.
    print("\nPor favor, digite as 4 notas do aluno (use ponto como separador decimal, se necessário):")
    
    # O loop 'for' executa o bloco de código 3 vezes (para nota 1, 2 e 3).
    for i in range(4):
        while True:
            try:
                # Solicita a nota. O f-string ajuda a mostrar o número da nota (i+1).
                nota = input(f"Digite a Nota {i + 1}: ")
                
                # Tenta converter a entrada (string) para um número de ponto flutuante (float).
                valor_nota = float(nota)
                
                # Garante que a nota é um valor válido (ex: entre 0 e 10).
                if 0 <= valor_nota <= 10:
                    notas_do_aluno.append(valor_nota) # Adiciona a nota à lista.
                    break # Sai do loop 'while' e passa para a próxima nota.
                else:
                    print("⚠️ Erro: A nota deve ser entre 0 e 10.")
            except ValueError:
                # É executado se a conversão para float falhar (ex: usuário digitou texto).
                print("⚠️ Erro: Por favor, digite um número válido.")

    # 3. Cálculo e Retorno de Status
    
    # Chama a função para obter a média.
    media_final = calcular_media(notas_do_aluno)
    
    # Define o critério de aprovação (7.0 como premissa).
    nota_minima_aprovacao = 7.0
    
    print("\n" + "="*30)
    print(f"Média Calculada: {media_final:.2f}") # Exibe a média com 2 casas decimais.
    
    # Condição para verificar a aprovação.
    if media_final >= nota_minima_aprovacao:
        print("🎉 STATUS: ALUNO APROVADO!")
    else:
        print("😢 STATUS: ALUNO REPROVADO.")
        
    print("="*30)

# Ponto de entrada do programa: A chamada à função principal.
if __name__ == "__main__":
    sistema_calculo_notas()