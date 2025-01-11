import requests
import allure
from config import BASE_URL, ENDPOINTS

class UserMethods:
    @staticmethod
    @allure.step("Регистрация нового пользователя")
    def register_user(email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(f"{BASE_URL}{ENDPOINTS['register_user']}", json=payload)
        return response

    @staticmethod
    @allure.step("Логин пользователя")
    def login_user(email, password):
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f"{BASE_URL}{ENDPOINTS['login_user']}", json=payload)
        return response

    @staticmethod
    @allure.step("Обновление данных пользователя")
    def update_user(token, new_data):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.patch(f"{BASE_URL}{ENDPOINTS['update_user']}", json=new_data, headers=headers)
        return response