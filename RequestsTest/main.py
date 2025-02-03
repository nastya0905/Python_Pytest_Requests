import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'cce37971d00964fec6638bf94d42ab3e'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}


body_create = {
    "name": "Бобр",
    "photo_id": 5
}

'''response = requests.post(url = f'{URL}/pokemons' , headers = HEADER, json = body_create )
print(response.text)'''

body_name = {
    "pokemon_id": "213695",
    "name": "New Name",
    "photo_id": 2
}

'''response = requests.patch(url = f'{URL}/pokemons' , headers = HEADER, json = body_name )
print(response.text)'''

body_pokebal ={
    "pokemon_id": "213695"
}

response_pokebal = requests.post(url= f'{URL}/trainers/add_pokeball' , headers= HEADER, json= body_pokebal) 
print(response_pokebal.text)



