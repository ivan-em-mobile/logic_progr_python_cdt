import requests
##Usando uma api de serie-animada ou retorna o valores definidos pelo usuario

def fetch_data(endpoint):
    response = requests.get(f'https://rickandmortyapi.com/api/{endpoint}')

##Check para responder o json ou vazio

    if response.status_code == 200:
        return response.json()
    else:
        return None

characters = fetch_data("character")

##Retorna os personagens ou ERROR:"Failed to fetch data"

if characters:
    print(characters)
else:
    print('Failed to fetch data')


print(characters)