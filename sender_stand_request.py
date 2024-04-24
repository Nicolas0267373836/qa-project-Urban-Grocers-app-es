import requests
import configuration
import data
from data import user_body


def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,  # Aquí se pasa el cuerpo JSON como argumento
                         headers=data.headers)


def get_auth_token():
    response = post_new_user(user_body)

    if response.status_code == 201:
        return response.json()["authToken"]
    else:
        return None


def create_client_kit(kit_body):
    auth_token = get_auth_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers)


def first_name():
    return "John"
