import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'fd1015a8ee77bc8b1497576fd1d41597'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '23384'



def test_status_code():
    response = requests.get(f'{URL}/v2/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200


def test_part_of_response():
    response_get = requests.get(f'{URL}/v2/trainers', params = {'trainer_id' : TRAINER_ID})  
    assert response_get.json()['data'][0]['id'] == '23384'