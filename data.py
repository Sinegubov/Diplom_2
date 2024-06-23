class URL:
    BASE_URL = "https://stellarburgers.nomoreparties.site"
    USER_REG_URL = f"{BASE_URL}/api/auth/register"
    USER_AUTH_URL = f"{BASE_URL}/api/auth/login"


class Messages:
    USER_BAD_INFO = "Email, password and name are required fields"
    USER_NO_UNIQ = "User already exists"
    USER_LOGIN_NO_USER = "email or password are incorrect"
