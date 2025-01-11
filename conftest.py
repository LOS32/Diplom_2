import pytest
from methods.user_methods import UserMethods
from config import USER_DATA

@pytest.fixture()
def register_user():
    # Попробуем удалить пользователя, если он существует
    login_response = UserMethods.login_user(
        USER_DATA["valid_user"]["email"],
        USER_DATA["valid_user"]["password"]
    )
    if login_response.status_code == 200:
        token = login_response.json()["accessToken"]
        UserMethods.delete_user(token)

    # Регистрируем пользователя
    response = UserMethods.register_user(
        USER_DATA["valid_user"]["email"],
        USER_DATA["valid_user"]["password"],
        USER_DATA["valid_user"]["name"]
    )
    assert response.status_code == 200, f"Failed to register user: {response.json()}"
    return USER_DATA["valid_user"]

@pytest.fixture()
def login_user(register_user):
    response = UserMethods.login_user(register_user["email"], register_user["password"])
    assert response.status_code == 200, f"Failed to login user: {response.json()}"
    token = response.json().get("accessToken")
    return token

@pytest.fixture()
def user_data():
    return {
        "email": "test_user@example.com",
        "password": "password123",
        "name": "Test User"
    }