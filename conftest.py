import pytest
import helpers
import requests
from data import URL


@pytest.fixture
def create_user():
    payload = helpers.UserGenerator().generate_user_info()
    response = requests.post(url=URL.USER_REG_URL, data=payload)

    yield response
    token = response.json()['accessToken']
    requests.delete(url=URL.USER_DELETE, headers={'Authorization': token})


@pytest.fixture
def user_data():
    payload = helpers.UserGenerator().generate_user_info()
    response = requests.post(url=URL.USER_REG_URL, data=payload)

    yield payload
    token = response.json()['accessToken']
    requests.delete(url=URL.USER_DELETE, headers={'Authorization': token})


@pytest.fixture
def user_token():
    payload = helpers.UserGenerator().generate_user_info()
    response = requests.post(url=URL.USER_REG_URL, data=payload)
    token = response.json()['accessToken']

    yield token
    requests.delete(url=URL.USER_DELETE, headers={'Authorization': token})

@pytest.fixture
def get_ingredient():
    response = requests.get(url=URL.INGREDIENT_GET)
    ingredient = response.json()["data"][1]["_id"]

    yield ingredient
