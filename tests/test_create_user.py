import allure
import requests
from data import Urls, Message
from helpers import generate_user_data


class TestCreateUser:
    @allure.title('Проверка создания уникального пользователя')
    def test_create_unique_user(self, create_user):
        response, data = create_user
        assert response.status_code == 200 and Message.SUCCESS_TRUE in response.text

    @allure.title("Проверка создания пользователя который уже зарегистрирован")
    def test_cannot_create_duplicate_user(self, create_user):
        response, data = create_user
        resp = requests.post(Urls.CREATE_USER, data=data)
        assert resp.status_code == 403 and Message.SUCCESS_FALSE in resp.text

    @allure.title("Проверка создания пользователя без обязательного поля 'имя'")
    def test_create_user_without_name(self):
        data = generate_user_data()
        data['name'] = ''
        resp = requests.post(Urls.CREATE_USER, data=data)
        assert resp.status_code == 403 and Message.REQUIRED_FIELDS in resp.text

    @allure.title("Проверка создания пользователя без обязательного поля 'пароль'")
    def test_create_user_without_password(self):
        data = generate_user_data()
        data['password'] = ''
        resp = requests.post(Urls.CREATE_USER, data=data)
        assert resp.status_code == 403 and Message.REQUIRED_FIELDS in resp.text

    @allure.title("Проверка создания пользователя без обязательного поля 'почта'")
    def test_create_user_without_email(self):
        data = generate_user_data()
        data['email'] = ''
        resp = requests.post(Urls.CREATE_USER, data=data)
        assert resp.status_code == 403 and Message.REQUIRED_FIELDS in resp.text
