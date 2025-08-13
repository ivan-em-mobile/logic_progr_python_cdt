import requests

"""
'endpoint': O que queremos buscar (tipo "personagens", "lugares", "episódios").
'filters': Uma lista de coisas que queremos filtrar (tipo "nome igual a Rick").
Se a gente não passar nenhum filtro, ela usa um dicionário vazio {}
"""

def fetch_data(endpoint, filters = {}):
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    response = requests.get(url, params=filters)
    
    return response.json()if response.status_code ==200 else None

"""
Depois de fazer o pedido, a API nos dá uma "resposta" (response).
A gente verifica o 'status_code' da resposta:
Se for '200', significa que o pedido foi "OK" e a API encontrou o que pedimos.
Aí a gente usa '.json()' para transformar a resposta (que vem em formato JSON)
em algo que o Python entende bem, tipo um dicionário.
Se não for 200 (tipo 404, que significa "não encontrado"), a gente retorna 'None' (nada).
"""

characters = fetch_data("character", {'name': 'Rick'})

"""
Retorna os personagens ou ERROR:"Failed to fetch data"
"""

if characters:
    print(characters)
else:
    print('Failed to fetch data')

print(characters)