from data.endpoints import AUTH_ENDPOINT

from utils.api_client import APIClient


api_client = APIClient()


def auth(auth_data=None):
    auth = api_client.post(AUTH_ENDPOINT, auth_data)
    return auth


def authorization(auth_data=None):
    auth = api_client.post(AUTH_ENDPOINT, auth_data)
    token = auth.json()['token']
    return token
    