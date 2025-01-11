BASE_URL = "https://stellarburgers.nomoreparties.site/api/"

ENDPOINTS = {
    "register_user": "auth/register",
    "login_user": "auth/login",
    "update_user": "auth/user",
    "create_order": "orders",
    "get_user_orders": "orders"
}

USER_DATA = {
    "valid_user": {
        "name": "Test User",
        "email": "test_user@mail.com",
        "password": "password123"
    },
    "duplicate_user": {
        "name": "Test User",
        "email": "test_user@mail.com",
        "password": "password123"
    }
}
