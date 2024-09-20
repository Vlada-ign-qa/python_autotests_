import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = 'e0210c92078e408d06faa458511ae5df'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}
TRAINER_ID = 5411

def test_status_code():
    response = requests.get(url=f'{URL}trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200