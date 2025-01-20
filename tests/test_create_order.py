import allure
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods
from config import USER_DATA, ORDER_DATA, SERVER_RESPONSES

@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth(self):
        login_response = UserMethods.login_user(
            USER_DATA["valid_user"]["email"],
            USER_DATA["valid_user"]["password"]
        )
        token = login_response.json().get("accessToken")
        order_response = OrderMethods.create_order(token, ORDER_DATA["valid_order"])
        assert order_response.status_code == 200 and SERVER_RESPONSES["order_created_key"]

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):
        order_response = OrderMethods.create_order(None, ORDER_DATA["valid_order"])
        assert order_response.status_code == 200 and SERVER_RESPONSES["order_created_key"]

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        login_response = UserMethods.login_user(
            USER_DATA["valid_user"]["email"],
            USER_DATA["valid_user"]["password"]
        )
        token = login_response.json().get("accessToken")
        order_response = OrderMethods.create_order(token, [])
        assert order_response.status_code == 400 and order_response.json()["message"] == SERVER_RESPONSES["ingredient_ids_missing"]

    @allure.title("Создание заказа с неверным хэшем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self):
        login_response = UserMethods.login_user(
            USER_DATA["valid_user"]["email"],
            USER_DATA["valid_user"]["password"]
        )
        token = login_response.json().get("accessToken")
        invalid_ingredients = ["invalid_hash_123"]
        order_response = OrderMethods.create_order(token, invalid_ingredients)
        assert order_response.status_code == SERVER_RESPONSES["server_error_code"]
