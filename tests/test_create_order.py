import allure
from methods.order_methods import OrderMethods
from config import USER_DATA, ORDER_DATA

@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth(self):
        login_response = OrderMethods.login_user(
            USER_DATA["valid_user"]["email"],
            USER_DATA["valid_user"]["password"]
        )
        token = login_response.json().get("accessToken")
        order_response = OrderMethods.create_order(token, ORDER_DATA["valid_order"])
        assert order_response.status_code == 200 and "order" in order_response.json(), (
            f"Expected status 200 and 'order' in response, but got {order_response.status_code} and {order_response.json()}"
        )

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):
        order_response = OrderMethods.create_order(None, ORDER_DATA["valid_order"])
        assert order_response.status_code == 200 and "order" in order_response.json(), (
            f"Expected status 200 and 'order' in response, but got {order_response.status_code} and {order_response.json()}"
        )

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        login_response = OrderMethods.login_user(
            USER_DATA["valid_user"]["email"],
            USER_DATA["valid_user"]["password"]
        )
        token = login_response.json().get("accessToken")
        order_response = OrderMethods.create_order(token, [])
        assert order_response.status_code == 400 and order_response.json()["message"] == "Ingredient ids must be provided", (
            f"Expected status 400 and message 'Ingredient ids must be provided', but got {order_response.status_code} and {order_response.json()}"
        )

    @allure.title("Создание заказа с неверным хэшем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self):
        login_response = OrderMethods.login_user(
            USER_DATA["valid_user"]["email"],
            USER_DATA["valid_user"]["password"]
        )
        token = login_response.json().get("accessToken")
        invalid_ingredients = ["invalid_hash_123"]
        order_response = OrderMethods.create_order(token, invalid_ingredients)
        assert order_response.status_code == 500, (
            f"Expected status 500, but got {order_response.status_code} and {order_response.json()}"
        )
