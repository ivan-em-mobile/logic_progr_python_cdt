import json

## 3° Atividade em Sala, iremos trabalhar com arquivos JSON, criando um arquivo com informações de frutas.E depois iremos ler
# as informações desse arquivo. Lembrando que é necessario criar um arquivo JSON com as informações das frutas. (frutas.json)

frutas = {
    'frutas': [
        {
            "fruta0": "maçã",
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

##Carregar e salvar JSON
# with open('frutas.json', 'r', encoding='utf-8') as arquivos:
#     dados = json.load(arquivos)
# print(dados)


##Escrever JSON
with open('frutas.json', 'w', encoding='utf-8') as arquivos:
    json.dump(frutas, arquivos, indent=8, ensure_ascii=False)  

#Salvamento com identação usando ASCII encoding

