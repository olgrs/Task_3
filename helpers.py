import requests
import random
import string
from data import REGISTER_URL, DELETE_USER_URL

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def create_user_via_api():
    """Создаёт пользователя через API и возвращает (email, password, name, token)."""
    email = f"test_{generate_random_string()}@example.com"
    password = generate_random_string()
    name = f"User_{generate_random_string()}"
    payload = {"email": email, "password": password, "name": name}
    response = requests.post(REGISTER_URL, json=payload)
    if response.status_code == 200 and response.json().get("success"):
        token = response.json().get("accessToken")
        return email, password, name, token
    return None, None, None, None

def delete_user_via_api(token):
    """Удаляет пользователя по токену."""
    requests.delete(DELETE_USER_URL, headers={"Authorization": token})