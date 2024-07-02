import pytest
import helpers
import requests
from data import URL


@pytest.fixture
def user_payload():
    payload = helpers.UserGenerator().generate_user_info()
    return payload


@pytest.fixture
def create_user(user_payload):
    response = requests.post(url=URL.USER_REG_URL, data=user_payload)
    token = response.json()["accessToken"]

    yield response, token
    requests.delete(url=URL.USER_DELETE, headers={"Authorization": token})


@pytest.fixture
def user_data(user_payload, create_user):
    yield user_payload


@pytest.fixture
def user_token(create_user):
    _, token = create_user

    yield token


@pytest.fixture
def get_ingredient():
    response = requests.get(url=URL.INGREDIENT_GET)
    ingredient = response.json()["data"][1]["_id"]

    yield ingredient
