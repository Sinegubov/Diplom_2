import requests
import allure
import pytest
from data import URL
from helpers import UserGenerator


@allure.feature('Проверка создания пользователя')
class TestPostOrderCreate:
    @allure.title('Проверка создания пользователя с уникальными данными')
    def test_user_create(self, url=URL.USER_REG_URL):
        payload = UserGenerator().generate_user_info()
        response = requests.post(url, data=payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Проверка создания неуникального пользователя с получением статуса 403')
    def test_user_create_no_uniq_user_negative(self, url=URL.USER_REG_URL):
        payload = UserGenerator().generate_user_info()
        requests.post(url, data=payload)
        response = requests.post(url, data=payload)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    @pytest.mark.parametrize("payload",
                             [
                                 ({
                                     "password": UserGenerator().generate_user_password(),
                                     "name": UserGenerator().generate_user_name()
                                 }),
                                 ({
                                     "email": UserGenerator().generate_user_email(),
                                     "name": UserGenerator().generate_user_name()
                                 }),
                                 ({
                                     "email": UserGenerator().generate_user_email(),
                                     "password": UserGenerator().generate_user_password()
                                 })
                             ])
    @allure.title('Проверка создания пользователя с недостающими данными')
    def test_user_create_bad_user_info(self, payload, url=URL.USER_REG_URL):
        response = requests.post(url, data=payload)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"
