import pytest
from methods.user_methods import UserMethods
from config import USER_DATA


@pytest.fixture()
def register_user():
    # Регистрируем пользователя
    response = UserMethods.register_user(
        USER_DATA["valid_user"]["email"],
        USER_DATA["valid_user"]["password"],
        USER_DATA["valid_user"]["name"]
    )
    # Возвращаем данные пользователя
    user_data = USER_DATA["valid_user"]

    # Используем yield для выполнения финализатора
    yield user_data

    # Финализатор: удаляем пользователя после завершения теста
    login_response = UserMethods.login_user(
        user_data["email"],
        user_data["password"]
    )
    if login_response.status_code == 200:
        token = login_response.json()["accessToken"]
        UserMethods.delete_user(token)

@pytest.fixture()
def login_user(register_user):
    response = UserMethods.login_user(register_user["email"], register_user["password"])
    assert response.status_code == 200, f"Failed to login user: {response.json()}"
    token = response.json().get("accessToken")
    return token

@pytest.fixture()
def user_data():
    return USER_DATA["valid_user"]