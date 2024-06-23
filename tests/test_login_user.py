import allure
import requests
from data import Urls, Message
from helpers import generate_user_data


class TestLoginUser:
    @allure.title("Проверка логина под существующим пользователем")
    def test_login_existing_user(self, create_user):
        response, data = create_user
        resp = requests.post(Urls.LOGIN_USER, data=data)
        assert resp.status_code == 200 and Message.SUCCESS_TRUE in resp.text

    @allure.title("Проверка логина с неверным емейл и паролем")
    def test_login_with_incorrect_data(self):
        data = generate_user_data()
        resp = requests.post(Urls.LOGIN_USER, data=data)
        assert resp.status_code == 401 and Message.INCORRECT_DATA

    @allure.title("Проверка логина с неверным паролем")
    def test_login_with_incorrect_password(self, create_user):
        response, data = create_user
        data['password'] = ''
        resp = requests.post(Urls.LOGIN_USER, data=data)
        assert resp.status_code == 401 and Message.INCORRECT_DATA

    @allure.title("Проверка логина с неверным емейл")
    def test_login_with_incorrect_email(self, create_user):
        response, data = create_user
        data['email'] = ''
        resp = requests.post(Urls.LOGIN_USER, data=data)
        assert resp.status_code == 401 and Message.INCORRECT_DATA
