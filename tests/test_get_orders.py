import allure
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods
from config import USER_DATA, USER_RESPONSES, SERVER_RESPONSES

@allure.feature("Получение заказов пользователя")
class TestGetOrders:

    @allure.title("Получение заказов авторизованным пользователем")
    def test_get_orders_with_auth(self):
        login_response = UserMethods.login_user(
            USER_DATA["registered_user"]["email"],
            USER_DATA["registered_user"]["password"]
        )
        token = login_response.json().get("accessToken")
        orders_response = OrderMethods.get_orders(token)
        assert orders_response.status_code == SERVER_RESPONSES["get_orders_status_code"] and SERVER_RESPONSES["get_orders_key"]

    @allure.title("Получение заказов неавторизованным пользователем")
    def test_get_orders_without_auth(self):
        orders_response = OrderMethods.get_orders(None)
        assert orders_response.status_code == SERVER_RESPONSES["unauthorized_status_code"] and orders_response.json()["message"] == SERVER_RESPONSES["unauthorized_message"]
