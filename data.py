class URL:
    BASE_URL = "https://stellarburgers.nomoreparties.site"
    USER_REG_URL = f"{BASE_URL}/api/auth/register"
    USER_AUTH_URL = f"{BASE_URL}/api/auth/login"
    USER_DELETE = f"{BASE_URL}/api/auth/user"
    USER_MODIFY_URL = f"{BASE_URL}/api/auth/user"
    ORDER_CREATE_URL = f"{BASE_URL}/api/orders"
    INGREDIENT_GET = f"{BASE_URL}/api/ingredients"


class Messages:
    USER_BAD_INFO = "Email, password and name are required fields"
    USER_NO_UNIQ = "User already exists"
    USER_LOGIN_NO_USER = "email or password are incorrect"
    USER_MODIFY_NO_AUTH = "You should be authorised"
    ORDER_NO_INGRED = "Ingredient ids must be provided"
    ORDER_NO_AUTH_USER = "You should be authorised"


class RawData:
    BAD_HASH = {"ingredients": ["111111111111111"]}
    BAD_TOKEN = {"Authorization": "111111111111111"}
    NO_INGRED  =  {"ingredients": []}
