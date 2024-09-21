import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'YOUR_TOKEN'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "YOUR_EMAIL",
    "password": "YOUR_PASSWORD"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_change_name = {
    "pokemon_id": "73043",
    "name": "Пупа",
    "photo_id": 2
}
body_add = {
    "pokemon_id": "73043"
}
body_knockout = {
    "pokemon_id": "73043"
}


'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

message_change_name = response_change_name.json()['message_change_name']
print(message_change_name)

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)

message_add = response_add.json()['message_add']
print(message_add)

'''response_knockout = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = body_knockout)
print(response_knockout.text)

message_knockout = response_knockout.json()['message_knockout']
print(message_knockout)'''