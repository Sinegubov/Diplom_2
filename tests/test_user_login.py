import requests
import allure

from data import URL, Messages
from helpers import UserGenerator


@allure.feature('Проверка авторизации пользователя')
class TestUserLogin:
    @allure.title('Проверка авторизации существующего пользователя')
    def test_user_login(self, url=URL.USER_AUTH_URL):
        payload = UserGenerator().generate_user_info()
        requests.post(url=URL.USER_REG_URL, data=payload)
        response = requests.post(url, data=payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка авторизации несуществующего пользователя')
    def test_user_login_no_exist_negative(self, url=URL.USER_AUTH_URL):
        payload = UserGenerator().generate_user_info()
        response = requests.post(url, data=payload)

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.USER_LOGIN_NO_USER
