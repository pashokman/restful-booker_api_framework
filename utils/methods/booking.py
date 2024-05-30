from data.endpoints import CREATE_BOOKING_ENDPOINT, GET_BOOKING_ENDPOINT, DELETE_BOOKING_ENDPOINT, GET_BOOKING_IDS_ENDPOINT, PARTIAL_UPDATE_BOOKING_ENDPOINT, UPDATE_BOOKING_ENDPOINT

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


def delete_booking_json(booking_id, token=None):
    headers = {'Cookie': f'token={token}'}
    delete = api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id), headers=headers)
    return delete.json()


def get_booking(booking_id):   
    get_resp = api_client.get(GET_BOOKING_ENDPOINT(booking_id))
    return get_resp


def get_booking_json(booking_id):   
    get_resp = api_client.get(GET_BOOKING_ENDPOINT(booking_id))
    return get_resp.json()


def get_booking_ids(params):
    get_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)
    return get_resp


def get_booking_ids_json(params):
    get_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)
    return get_resp.json()


def update_booking(booking_id, data, token=None):
    headers = {'Cookie': f'token={token}'}
    part_upd_resp = api_client.put(UPDATE_BOOKING_ENDPOINT(booking_id), data, headers)
    return part_upd_resp


def partial_update_boking(booking_id, data, token=None):
    headers = {'Cookie': f'token={token}'}
    part_upd_resp = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), data, headers)
    return part_upd_resp


def partial_update_boking_json(booking_id, data, token=None):
    headers = {'Cookie': f'token={token}'}
    part_upd_resp = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), data, headers)
    return part_upd_resp.json()
