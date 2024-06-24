import requests
import allure

from data import URL, Messages, RawData


@allure.feature("Проверка создания заказа")
class TestOrderCreate:
    @allure.title("Проверка создания заказа  с авторизацией с валидным хэшем ингредиентов")
    def test_auth_user_create_order_successful(self, user_token, get_ingredient, url=URL.ORDER_CREATE_URL):
        token = user_token
        ingredient = get_ingredient
        response = requests.post(url, headers={"Authorization": token}, data={"ingredients": ingredient})

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["order"]["number"] > 0

    @allure.title("Проверка создания заказа без авторизации с валидным хэшем ингредиентов")
    def test_no_auth_user_create_order_successful(self, get_ingredient, url=URL.ORDER_CREATE_URL):
        ingredient = get_ingredient
        response = requests.post(url, data={"ingredients": ingredient})

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["order"]["number"] > 0

    @allure.title("Проверка создания заказа с авторизацией и без ингредиентов")
    def test_auth_user_create_order_without_ingredient_negative(self, user_token, url=URL.ORDER_CREATE_URL):
        token = user_token
        response = requests.post(url, headers={"Authorization": token})

        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.ORDER_NO_INGRED

    @allure.title("Проверка создания без авторизации и без ингредиентов")
    def test_no_auth_user_create_order_without_ingredient_negative(self, url=URL.ORDER_CREATE_URL):
        response = requests.post(url)

        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.ORDER_NO_INGRED

    @allure.title("Проверка создания заказа без авторизации с невалидным хэшем ингредиентов")
    def test_order_create_bad_hash_ingredient_negative(self, url=URL.ORDER_CREATE_URL):
        response = requests.post(url, data=RawData.BAD_HASH)

        assert response.status_code == 500 and "Internal Server Error" in response.text
