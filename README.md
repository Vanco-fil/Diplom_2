## Дипломный проект. Задание 2: API

### Тестируем ручки API для сайта [Stellar Burgers](https://stellarburgers.nomoreparties.site)

### [Документация API](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89)

### Структура проекта

- `conftest` - Cтартовая фикстура c генерацией данных для создание пользователя, после теста пользователь удаляется
- `tests` - Пакет, содержащий тесты
- `data` - Содержит cтатические данные для тестов
- `allure_results` - Содержит отчеты по тестированию 
- `helpers` - Содержит вспомогательные методы, которые помогают генерировать данные

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Можно установить в ручную библиотеки pytest,  requests и allure-pytest**

>  `$ pip install pytest`
> 
>  `$ pip install allure-pytest`
> 
>  `$ pip install requests` 

**Запустить все автотесты**

>  `$ pytest tests`

**Генерация отчета в формате веб-страницы**

>  `$ allure serve allure_results `