import allure
from methods.user_methods import UserMethods
from config import USER_DATA, USER_RESPONSES

@allure.feature("Логин пользователя")
class TestLoginUser:
    @allure.feature("Логин пользователя")
    class TestLoginUser:

        @allure.title("Тест на логин с валидными данными")
        def test_login_valid_user(self):
            response = UserMethods.login_user(
                USER_DATA["registered_user"]["email"],
                USER_DATA["registered_user"]["password"]
            )
            response_json = response.json()
            assert "accessToken" in response_json, f"Response does not contain 'accessToken': {response_json}"

    @allure.title("Логин с неверным email")
    def test_login_invalid_email(self):
        response = UserMethods.login_user(
            USER_DATA["login_with_invalid_email"]["email"],
            USER_DATA["login_with_invalid_email"]["password"]
        )
        assert response.status_code == 401 and response.json()["message"] == USER_RESPONSES["login_incorrect"], (
            f"Expected status 401 and message '{USER_RESPONSES['login_incorrect']}', but got {response.status_code} and {response.json()}"
        )

    @allure.title("Логин с неверным паролем")
    def test_login_invalid_password(self):
        response = UserMethods.login_user(
            USER_DATA["login_with_invalid_password"]["email"],
            USER_DATA["login_with_invalid_password"]["password"]
        )
        assert response.status_code == 401 and response.json()["message"] == USER_RESPONSES["login_incorrect"], (
            f"Expected status 401 and message '{USER_RESPONSES['login_incorrect']}', but got {response.status_code} and {response.json()}"
        )
