import requests
import json

def create_pokemon():

    body = {"name":"name", 
        "photo":"https://dolnikov.ru/pokemons/albums/123.png"}
    response = requests.post("https://pokemonbattle.me:9104/pokemons",
                            data=json.dumps(body), 
                            headers={"trainer_token": "",
                                     'content-type': 'application/json'})
    
    b_list = json.loads(response.content)
    pok_id = b_list["id"]
    print(response.json())
    return pok_id

def change_name(id):
    body = {
        "pokemon_id": id,
        "name": "New Name",
        "photo": "https://dolnikov.ru/pokemons/albums/123.png"}
    response = requests.put('https://pokemonbattle.me:9104/pokemons',
                            data=json.dumps(body), 
                            headers={"trainer_token": "",
                                     'content-type': 'application/json'})
    print(response.json())


def put_in_pokeball_func(pok_id):
    body = {"pokemon_id": pok_id}
    response = requests.post("https://pokemonbattle.me:9104/trainers/add_pokeball",
                            data=json.dumps(body), 
                            headers={"trainer_token": "",
                                     'content-type': 'application/json'})
    print(response.json())

pok_id = create_pokemon()
change_name(pok_id)
put_in_pokeball_func(pok_id)
