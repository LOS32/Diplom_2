import allure
from methods.order_methods import OrderMethods
from config import USER_DATA, USER_RESPONSES

@allure.feature("Получение заказов пользователя")
class TestGetOrders:

    @allure.title("Получение заказов авторизованным пользователем")
    def test_get_orders_with_auth(self):
        login_response = OrderMethods.login_user(
            USER_DATA["valid_user"]["email"],
            USER_DATA["valid_user"]["password"]
        )
        token = login_response.json().get("accessToken")
        orders_response = OrderMethods.get_orders(token)
        assert orders_response.status_code == 200 and "orders" in orders_response.json(), (
            f"Expected status 200 and 'orders' in response, but got {orders_response.status_code} and {orders_response.json()}"
        )

    @allure.title("Получение заказов неавторизованным пользователем")
    def test_get_orders_without_auth(self):
        orders_response = OrderMethods.get_orders(None)
        assert orders_response.status_code == 401 and orders_response.json()["message"] == USER_RESPONSES["unauthorized"], (
            f"Expected status 401 and message '{USER_RESPONSES['unauthorized']}', but got {orders_response.status_code} and {orders_response.json()}"
        )
