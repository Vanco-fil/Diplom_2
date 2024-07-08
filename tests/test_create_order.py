import allure
import requests
from data import Urls, Message, Ingredients


class TestCreateOrder:
    @allure.title("Проверка создания заказа с авторизацией и ингредиентами")
    def test_create_order_auth_user_ingredients(self, create_user):
        response, data = create_user
        requests.post(Urls.LOGIN_USER, data=data)
        ingredients = {"ingredients": [Ingredients.FLUOR_BUN, Ingredients.BIO_CUTLET, Ingredients.SAUCE_SPICY, Ingredients.FLUOR_BUN]}
        resp = requests.post(Urls.CREATE_ORDER, data=ingredients)
        assert resp.status_code == 200 and Message.SUCCESS_TRUE in resp.text

    @allure.title("Проверка создания заказа без авторизации и с ингредиентами")
    def test_create_order_not_auth_user_ingredients(self):
        ingredients = {"ingredients": [Ingredients.FLUOR_BUN, Ingredients.BIO_CUTLET, Ingredients.SAUCE_SPICY, Ingredients.FLUOR_BUN]}
        resp = requests.post(Urls.CREATE_ORDER, data=ingredients)
        assert resp.status_code == 200 and Message.SUCCESS_TRUE in resp.text

    @allure.title("Проверка создания заказа с авторизацией и без ингредиентов")
    def test_create_order_auth_user_without_ingredients(self, create_user):
        response, data = create_user
        requests.post(Urls.LOGIN_USER, data=data)
        ingredients = {"ingredients": ['']}
        resp = requests.post(Urls.CREATE_ORDER, data=ingredients)
        assert resp.status_code == 400 and Message.NOT_INGREDIENT in resp.text

    @allure.title("Проверка создания заказа без авторизации и неверным хешем ингредиентов")
    def test_create_order_not_auth_user_incorrect_hash(self):
        ingredients = {"ingredients": [Ingredients.INVALID_HASH, Ingredients.FLUOR_BUN, Ingredients.BIO_CUTLET]}
        resp = requests.post(Urls.CREATE_ORDER, data=ingredients)
        assert resp.status_code == 500 and Message.ORDER_INCORRECT_INGREDIENTS in resp.text
