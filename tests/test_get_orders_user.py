import allure
import requests
from data import Urls, Message, Ingredients


class TestGetOrdersUser:
    @allure.title("Проверка получения заказа авторизованным пользователем")
    def test_get_order_auth_user(self, create_user):
        response, data = create_user
        token = response.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        ingredients = {"ingredients": [Ingredients.FLUOR_BUN, Ingredients.BIO_CUTLET, Ingredients.SAUCE_SPICY, Ingredients.FLUOR_BUN]}
        requests.post(Urls.CREATE_ORDER, data=ingredients, headers=headers)
        order = requests.get(Urls.GET_ORDER, headers=headers)
        assert order.status_code == 200 and Message.SUCCESS_TRUE in order.text

    @allure.title("Проверка получения заказа неавторизованным пользователем")
    def test_get_order_not_auth_user(self):
        order = requests.get(Urls.GET_ORDER)
        assert order.status_code == 401 and Message.ORDER_NOT_AUTHORIZED in order.text
