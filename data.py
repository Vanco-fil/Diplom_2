class Urls:
    URL = "https://stellarburgers.nomoreparties.site"
    CREATE_USER = f"{URL}/api/auth/register"
    DELETE_USER = f"{URL}/api/auth/user"
    LOGIN_USER = f"{URL}/api/auth/login"
    UPDATE_DATA = f"{URL}/api/auth/user"
    CREATE_ORDER = f"{URL}/api/orders"
    GET_ORDER = f"{URL}/api/orders"


class Message:
    SUCCESS_TRUE = '"success":true'
    SUCCESS_FALSE = '"success":false'
    REQUIRED_FIELDS = "Email, password and name are required fields"
    INCORRECT_DATA = "email or password are incorrect"
    NOT_AUTHORIZED = "You should be authorised"
    NOT_INGREDIENT = "Ingredient ids must be provided"
    ORDER_INCORRECT_INGREDIENTS = "Internal Server Error"
    ORDER_NOT_AUTHORIZED = "You should be authorised"


class Ingredients:
    FLUOR_BUN = "61c0c5a71d1f82001bdaaa6d"
    BIO_CUTLET = '61c0c5a71d1f82001bdaaa71'
    SAUCE_SPICY = '61c0c5a71d1f82001bdaaa72'
    INVALID_HASH = '11c1c1a11d1f11001bdaaa1'
