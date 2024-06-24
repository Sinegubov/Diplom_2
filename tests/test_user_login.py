import requests
import allure

from data import URL, Messages
from helpers import UserGenerator


@allure.feature("Проверка авторизации пользователя")
class TestUserLogin:
    @allure.title('Проверка авторизации существующего пользователя')
    def test_exist_user_login(self, user_data, url=URL.USER_AUTH_URL):
        payload = user_data
        response = requests.post(url, data=payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Проверка авторизации c неверным логином и паролем")
    def test_user_login_no_exist_negative(self, url=URL.USER_AUTH_URL):
        payload = UserGenerator().generate_user_info()
        response = requests.post(url, data=payload)

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.USER_LOGIN_NO_USER
