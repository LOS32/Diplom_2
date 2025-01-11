import allure
from methods.user_methods import UserMethods
from config import USER_DATA, USER_RESPONSES

@allure.feature("Изменение данных пользователя")
class TestUserDataUpdate:

    @allure.title("Обновление данных пользователя с авторизацией")
    def test_update_user_with_auth(self):
        UserMethods.register_user(
            USER_DATA["valid_user"]["email"],
            USER_DATA["valid_user"]["password"],
            USER_DATA["valid_user"]["name"]
        )
        login_response = UserMethods.login_user(
            USER_DATA["valid_user"]["email"],
            USER_DATA["valid_user"]["password"]
        )
        token = login_response.json().get("accessToken")
        new_data = {
            "name": "Updated Name"
        }
        update_response = UserMethods.update_user(token, new_data)
        assert update_response.status_code == 200 and update_response.json()["user"]["name"] == USER_DATA["update_user"]["name"]

    @allure.title("Обновление данных пользователя без авторизации")
    def test_update_user_without_auth(self):
        new_data = {
            "name": "Updated Name",
            "email": "updated_user@example.com"
        }
        update_response = UserMethods.update_user(None, new_data)
        assert update_response.status_code == 401 and update_response.json()["message"] == USER_RESPONSES["unauthorized"]
