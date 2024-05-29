from data.endpoints import CREATE_BOOKING_ENDPOINT, GET_BOOKING_ENDPOINT, DELETE_BOOKING_ENDPOINT
from utils.api_client import APIClient


api_client = APIClient()


def create_booking(booking_data):
    booking = api_client.post(CREATE_BOOKING_ENDPOINT, booking_data)
    return booking


def create_booking_json(booking_data):
    booking = api_client.post(CREATE_BOOKING_ENDPOINT, booking_data)
    return booking.json()


def delete_booking(booking_id, token=None):
    headers = {'Cookie': f'token={token}'}
    delete = api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id), headers=headers)
    return delete


def delete_booking_json(booking_id, token):
    headers = {'Cookie': f'token={token}'}
    delete = api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id), headers=headers)
    return delete.json()


def get_booking(booking_id):   
    get_resp = api_client.get(GET_BOOKING_ENDPOINT(booking_id))
    return get_resp


def get_booking_json(booking_id):   
    get_resp = api_client.get(GET_BOOKING_ENDPOINT(booking_id))
    return get_resp.json()