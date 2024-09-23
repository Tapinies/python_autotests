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
    "pokemon_id": "74046",
    "name": "Пупа",
    "photo_id": 2
}
body_add = {
    "pokemon_id": "74046"
}
body_knockout = {
    "pokemon_id": "74046"
}

# Регистрируемся
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

# Подтверждаем регистрацию
'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

# Создаем покемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

# Меняем имя и изображение покемона
response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

message_change_name = response_change_name.json()['message']
print(message_change_name)

# Ловим покемона
response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)

message_add = response_add.json()['message'] 
print(message_add)

# Нокаутируем покемона
'''response_knockout = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = body_knockout)
print(response_knockout.text)

message_knockout = response_knockout.json()['message']
print(message_knockout)'''