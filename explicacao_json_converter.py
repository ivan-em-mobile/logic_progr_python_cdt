import json

## 2° Atividade em Sala, iremos trabalhar com arquivos JSON, criando um arquivo com informações sobre os clientes e serviços
# mas em um formato de lista = dump.

dados = {'nome': 'Joao Silva', 'idade': 30, 'cidade': 'Sao Paulo', 'servico': 'Premium'}

json_string = json.dumps(dados)
# Imprimindo o dicionário inteiro como uma string JSON

print(json_string)
# Imprimindo o dicionário inteiro

# print(dados)