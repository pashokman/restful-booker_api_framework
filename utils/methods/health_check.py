from data.endpoints import HEALTH_CHECK_ENDPOINT

from utils.api_client import APIClient


def health_check():
    api_client = APIClient()
    health_check = api_client.get(HEALTH_CHECK_ENDPOINT)
    return health_check
