import allure
import requests
from data import URL, Messages, RawData


@allure.feature("Проверка получения заказов конкретного пользователя")
class TestGetUserOrder:
    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_auth_user_orders(self, user_token, url=URL.ORDER_CREATE_URL):
        token = user_token
        response = requests.get(url, headers={'Authorization': token})

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["total"] > 0

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_no_auth_user_orders_negative(self, user_token, url=URL.ORDER_CREATE_URL):
        response = requests.get(url, headers=RawData.BAD_TOKEN)

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == Messages.ORDER_NO_AUTH_USER
