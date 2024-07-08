import pytest
import requests
from helpers import generate_user_data
from data import Urls


@pytest.fixture(scope='function')
def create_user():
    data = generate_user_data()
    response = requests.post(Urls.CREATE_USER, data=data)
    token = response.json()['accessToken']
    headers = {"Content-type": "application/json", "Authorization": f'{token}'}
    yield response, data
    requests.delete(Urls.DELETE_USER, headers=headers)
