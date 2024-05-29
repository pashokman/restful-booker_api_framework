from data.endpoints import AUTH_ENDPOINT


def authorization(api_client, auth_data):
    auth = api_client.post(AUTH_ENDPOINT, auth_data)
    token = auth.json()['token']
    
    return token
    