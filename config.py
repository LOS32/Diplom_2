BASE_URL = "https://stellarburgers.nomoreparties.site/api/"

ENDPOINTS = {
    "register_user": "auth/register",
    "login_user": "auth/login",
    "update_user": "auth/user",
    "create_order": "orders",
    "get_user_orders": "orders",
    "get_orders": "orders"
}

USER_DATA = {
    "valid_user": {
        "name": "Test_User",
        "email": "test_user@mail.com",
        "password": "password123"
    },
    "duplicate_user": {
        "name": "Test User",
        "email": "test_user@mail.com",
        "password": "password123"
    },
    "login_with_invalid_email": {
        "email": "invalid_email@example.com",
        "password": "password123"
    },
    "login_with_invalid_password": {
        "email": "test_user@example.com",
        "password": "wrong_password"
    },
    "missing_email": {
        "password": "password123",
        "name": "Test User"
    },
    "missing_password": {
        "email": "test_user@example.com",
        "name": "Test User"
    },
    "update_user": {
        "email": "updated_user@example.com",
        "name": "Updated Name"
    },
    "registered_user": {
        "email": "Dmitrii_Losunov_15_963@yandex.ru",
        "password": "123456"
    }
}

USER_RESPONSES = {
    "login_incorrect": "email or password are incorrect",
    "user_already_exists": "User already exists",
    "missing_data": "Email, password and name are required fields",
    "unauthorized": "You should be authorised"
}

ORDER_DATA = {
    "valid_order": [
        "61c0c5a71d1f82001bdaaa6d",
        "61c0c5a71d1f82001bdaaa6f",
        "61c0c5a71d1f82001bdaaa70"
    ]
}