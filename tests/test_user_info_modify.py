import requests
import pytest
import allure

from data import URL, Messages
from helpers import UserGenerator


@allure.feature('Проверка изменения данных пользователя')
class TestUserInfoModify:
    @pytest.mark.parametrize("payload", [
        {"password": UserGenerator().generate_user_password()},
        {"name": UserGenerator().generate_user_name()},
        {"email": UserGenerator().generate_user_email()}
    ])
    @allure.title('Проверка изменения данных пользователя с авторизацией')
    def test_user_modify_user_info(self, user_token, payload, url=URL.USER_MODIFY_URL):
        access_token = user_token
        response = requests.patch(url, headers={'Authorization': access_token}, data=payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @pytest.mark.parametrize("payload", [
        {"password": UserGenerator().generate_user_password()},
        {"name": UserGenerator().generate_user_name()},
        {"email": UserGenerator().generate_user_email()}
    ])
    @allure.title('Проверка изменения данных пользователя без авторизации')
    def test_user_modify_user_info_no_auth_negative(self, payload, url=URL.USER_MODIFY_URL):
        response = requests.patch(url, data=payload)

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.USER_MODIFY_NO_AUTH
