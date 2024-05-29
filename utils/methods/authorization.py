from data.endpoints import AUTH_ENDPOINT
from utils.api_client import APIClient


def authorization(auth_data):
    api_client = APIClient()
    auth = api_client.post(AUTH_ENDPOINT, auth_data)
    token = auth.json()['token']
    
    return token
    