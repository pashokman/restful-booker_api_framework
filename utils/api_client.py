import requests
from utils.config import BASE_URL

class APIClient():
    def __init__(self, base_url = BASE_URL):
        self.base_url = base_url

    def post(self, endpoint, data=None, headers=None):
        url = f'{self.base_url}{endpoint}'
        return requests.post(url, json=data, headers=headers)
    
    def get(self, endpoint, headers=None, params=None):
        url = f'{self.base_url}{endpoint}'
        return requests.get(url, headers=headers, params=params)

    def put(self, endpoint, data=None, headers=None):
        url = f'{self.base_url}{endpoint}'
        return requests.put(url, json=data, headers=headers)

    def patch(self, endpoint, data=None, headers=None):
        url = f'{self.base_url}{endpoint}'
        return requests.patch(url, json=data, headers=headers)

    def delete(self, endpoint, data=None, headers=None):
        url = f'{self.base_url}{endpoint}'
        return requests.delete(url, json=data, headers=headers)