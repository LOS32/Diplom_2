import allure
import pytest
from methods.user_methods import UserMethods
from helpers import generate_random_user
from config import USER_DATA

@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Регистрация уникального пользователя")
    def test_register_unique_user(self, user_data):
        user_data = generate_random_user()
        response = UserMethods.register_user(user_data["email"], user_data["password"], user_data["name"])
        assert response.status_code == 200 and response.json()["success"] is True, (
            f"Expected status 200 and success True, but got {response.status_code} and {response.json()}"
        )

    @allure.title("Регистрация пользователя с уже существующим email")
    def test_register_existing_user(self):
        user_methods = UserMethods()
        user_methods.register_user(
            USER_DATA["valid_user"]["email"],
            USER_DATA["valid_user"]["password"],
            USER_DATA["valid_user"]["name"]
        )
        response = user_methods.register_user(
            USER_DATA["duplicate_user"]["email"],
            USER_DATA["duplicate_user"]["password"],
            USER_DATA["duplicate_user"]["name"]
        )
        assert response.status_code == 403 and response.json()["message"] == "User already exists", (
            f"Expected status 403 and message 'User already exists', but got {response.status_code} and {response.json()}"
        )

    @allure.title("Регистрация пользователя без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_register_user_missing_field(self, missing_field, user_data):
        user_data.pop(missing_field)
        response = UserMethods.register_user(
            user_data.get("email", ""),
            user_data.get("password", ""),
            user_data.get("name", "")
        )
        assert response.status_code == 403 and response.json()["message"] == "Email, password and name are required fields", (
            f"Expected status 403 and message 'Email, password and name are required fields', but got {response.status_code} and {response.json()}"
        )
