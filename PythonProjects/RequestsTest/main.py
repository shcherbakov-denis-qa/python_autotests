import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'fd1015a8ee77bc8b1497576fd1d41597'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_regitration = {
    "trainer_token": TOKEN,
    "email": "ya.denisqee@yandex.ru",
    "password": "Denis123"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "170226",
    "name": "ЗдароваНачальнмк",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "170226"
}

'''response = requests.post(url = f'{URL}/v2/trainers/reg', headers = HEADER, json = body_regitration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/v2/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''


'''response_create = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''


'''response_change = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_change )
print(response_change.text)'''

response_pokeball = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)
