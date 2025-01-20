import allure
import pytest
from methods.user_methods import UserMethods
from helpers import generate_random_user
from config import USER_DATA, CREATE_USER_RESPONSES

@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Регистрация уникального пользователя")
    def test_register_unique_user(self, user_data):
        user_data = generate_random_user()
        response = UserMethods.register_user(user_data["email"], user_data["password"], user_data["name"])
        assert response.status_code == CREATE_USER_RESPONSES["success_status_code"] and response.json()[CREATE_USER_RESPONSES["success_key"]] is CREATE_USER_RESPONSES["success_value"]

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
        assert response.status_code == CREATE_USER_RESPONSES["user_exists_status_code"] and response.json()["message"] == CREATE_USER_RESPONSES["user_exists_message"]

    @allure.title("Регистрация пользователя без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_register_user_missing_field(self, missing_field, user_data):
        user_data.pop(missing_field)
        response = UserMethods.register_user(
            user_data.get("email", ""),
            user_data.get("password", ""),
            user_data.get("name", "")
        )
        assert response.status_code == CREATE_USER_RESPONSES["missing_fields_status_code"] and response.json()["message"] == CREATE_USER_RESPONSES["missing_fields_message"]
