import pytest
from methods.user_methods import UserMethods
from config import USER_DATA

@pytest.fixture()
def register_user(user_data):
    user_data = USER_DATA["valid_user"]
    response = UserMethods.register_user(user_data["email"], user_data["password"], user_data["name"])
    assert response.status_code == 200, f"Failed to register user: {response.json()}"
    login_response = UserMethods.login_user(user_data["email"], user_data["password"])
    assert login_response.status_code == 200, f"Failed to login user: {login_response.json()}"
    token = login_response.json().get("accessToken")
    yield user_data
    UserMethods.delete_user(token)

@pytest.fixture()
def login_user(register_user):
    response = UserMethods.login_user(register_user["email"], register_user["password"])
    assert response.status_code == 200, f"Failed to login user: {response.json()}"
    token = response.json().get("accessToken")
    return token

@pytest.fixture()
def user_data():
    return {
        "email": "test_user@example.com",
        "password": "password123",
        "name": "Test User"
    }