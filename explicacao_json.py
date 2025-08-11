import json

## 1° Atividade em Sala, iremos trabalhar com arquivos JSON, criando um arquivo com informações de clientes e tipo de 
# serviço. Também teremos alguns questionários para preencher.

json_string = """
{
  "nome": "João Silva",
  "idade": 30,
  "cidade": "São Paulo",
  "servico": "Premium"
}
"""

dados = json.loads(json_string)

##Qual a diferença entre o uso do for para printar os dados?
# A diferença entre os dois métodos de impressão é que o primeiro 
# usa um loop para iterar sobre cada chave e valor do dicionário,
# enquanto o segundo imprime o dicionário inteiro de uma vez.
# O primeiro método permite um controle mais fino sobre a formatação da saída,
# enquanto o segundo simplesmente exibe o dicionário como um todo.
# Usando um loop for para imprimir cada chave e valor


# for chave, valor in dados.items():
#     print(f"{chave}: {valor}")

# print(dados)
# print('\n')