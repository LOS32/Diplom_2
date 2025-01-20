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

CREATE_USER_RESPONSES = {
    # Регистрация уникального пользователя
    "success_key": "success",
    "success_value": True,
    "success_status_code": 200,
    # Регистрация пользователя с уже существующим email
    "user_exists_status_code": 403,
    "user_exists_message": "User already exists",
    # Регистрация пользователя без обязательного поля
    "missing_fields_status_code": 403,
    "missing_fields_message": "Email, password and name are required fields"
}

USER_RESPONSES = {
    "login_incorrect": "email or password are incorrect",
    "user_already_exists": "User already exists",
    "missing_data": "Email, password and name are required fields",
    "unauthorized": "You should be authorised"
}

SERVER_RESPONSES = {
    # Создание заказа с авторизацией и ингредиентами
    "order_created_key": "order",
    # Создание заказа без ингредиентов
    "ingredient_ids_missing": "Ingredient ids must be provided",
    # Создание заказа с неверным хэшем ингредиентов
    "server_error_code": 500,
    # Получение заказов авторизованным пользователем
    "get_orders_status_code": 200,
    "get_orders_key": "orders",
    # Получение заказов неавторизованным пользователем
    "unauthorized_status_code": 401,
    "unauthorized_message": "You should be authorised",
    #
    "access_token_key": "accessToken"
}

ORDER_DATA = {
    "valid_order": [
        "61c0c5a71d1f82001bdaaa6d",
        "61c0c5a71d1f82001bdaaa6f",
        "61c0c5a71d1f82001bdaaa70"
    ]
}