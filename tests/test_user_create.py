import requests
import allure
import pytest

from data import URL, Messages
from helpers import UserGenerator


@allure.feature("Проверка создания пользователя")
class TestUserCreate:
    @allure.title("Проверка создания пользователя с уникальными данными")
    def test_user_create(self, user_payload, url=URL.USER_REG_URL):
        payload = user_payload
        response = requests.post(url, data=payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Проверка создания неуникального пользователя с получением статуса 403")
    def test_user_create_no_uniq_user_negative(self, user_payload, url=URL.USER_REG_URL):
        payload = user_payload
        requests.post(url, data=payload)
        response = requests.post(url, data=payload)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.USER_NO_UNIQ

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
    @allure.title("Проверка создания пользователя с недостающими данными")
    def test_user_create_bad_user_info(self, payload, url=URL.USER_REG_URL):
        response = requests.post(url, data=payload)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.USER_BAD_INFO
