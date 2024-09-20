import requests

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'e0210c92078e408d06faa458511ae5df'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_put = {
    "pokemon_id": "72967",
    "name": "New Name",
    "photo_id": 2
}

body_add = {
    "pokemon_id": "72967"
}

'''response_create = requests.post(url=f'{URL}pokemons', headers=HEADER, json=body_create)
print(response_create.text)'''

'''response_put = requests.put(url=f'{URL}pokemons', headers=HEADER, json=body_put)
print(response_put.text)'''

response_add = requests.post(url=f'{URL}trainers/add_pokeball', headers=HEADER, json=body_add)
print(response_add.text)