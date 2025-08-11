# import json

# json_string = """[

# {
# "nome_moto":"yamaha factor 150",
# "ano":"2020/2021",
# "cor":"preto",
# "cilindradas":150,
# "combustiveis":["gasolina","etanol"]
# },
# {
# "nome_moto":"honda cb 500",
# "ano":"2020/2021",
# "cor":"vermelho",
# "cilindradas":500,
# "combustiveis":["gasolina","etanol"]
# },
# {
# "nome_moto":"suzuki gsx 750",
# "ano":"2020/2021",
# "cor":"azul",
# "cilindradas":750,
# "combustiveis":["gasolina","etanol"]
# }

# ]

# """
# dados = json.loads(json_string)
# ##loads, serve para converter a string JSON em um objeto Python 
# # (neste caso, uma lista de dicionários)

# print(dados)
# print('\n')



# import json

# dados = {'nome': 'Joao Silva', 'idade': 30, 
#          'cidade': 'Sao Paulo', 'servico': 'Premium'}



# json_string = json.dumps(dados)
# # Imprimindo o dicionário inteiro como uma string JSON

# print(json_string)
# # Imprimindo o dicionário inteiro

# # print(dados)



import json

frutas = {
    'frutas': [
        {
            "fruta1": "maçã",
            "preco": 2.34,
        },
        {
            "fruta1": "pera",
            "preco": 3.45,
        },
        {
            "fruta2": "banana",
            "preco": 1.23,
        },
        {
            "fruta3": "laranja",
            "preco": 4.56
        }
    ]
}

##Escrever JSON
with open('frutas.json', 'w', encoding='utf-8') as arquivos:
    json.dump(frutas, arquivos, indent=8, ensure_ascii=False)  

##Salvamento com identação usando ASCII encoding
