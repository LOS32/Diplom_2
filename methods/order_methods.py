import requests
import allure
from config import BASE_URL, ENDPOINTS

class OrderMethods:

    @staticmethod
    @allure.step("Создание заказа")
    def create_order(token, ingredients):
        headers = {"Authorization": token} if token else {}
        payload = {"ingredients": ingredients}
        response = requests.post(f"{BASE_URL}{ENDPOINTS['create_order']}", json=payload, headers=headers)
        return response

    @staticmethod
    @allure.step("Получение заказов пользователя")
    def get_orders(token):
        headers = {"Authorization": token} if token else {}
        response = requests.get(f"{BASE_URL}{ENDPOINTS['get_orders']}", headers=headers)
        return response
