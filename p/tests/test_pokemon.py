import requests
import json

def test_resp_stat_get_trainer():
    response = requests.get('https://pokemonbattle.me:9104/trainers?trainer_id=4356')
    assert response.status_code == 200

def test_name_my_trainer():
    response = requests.get('https://pokemonbattle.me:9104/trainers?trainer_id=4356')
    blist = json.loads(response.content)
    train_name = blist['trainer_name']
    assert train_name == 'ПенсионерПрод'