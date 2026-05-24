import requests
import random
import string
from data import REGISTER_URL, DELETE_USER_URL


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def create_user_via_api():
    email = f"test_{generate_random_string()}@example.com"
    password = generate_random_string()
    name = f"User_{generate_random_string()}"

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(REGISTER_URL, json=payload)

    if response.status_code == 200 and response.json().get("success"):
        return email, password, response.json().get("accessToken")

    raise AssertionError("User creation via API failed")


def delete_user_via_api(token):
    if not token:
        return

    requests.delete(
        DELETE_USER_URL,
        headers={"Authorization": token}
    )
