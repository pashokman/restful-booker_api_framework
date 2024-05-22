import pytest
from data.endpoints import GET_BOOKING_IDS_ENDPOINT


@pytest.mark.get_booking_ids
def test_get_booking_ids_by_non_existing_firstname(api_client):
    params = {'firstname': 'Pop'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)

    err_msg = f'Response body is not empty - {ids_resp.json()}'
    assert ids_resp.json() == [], err_msg


@pytest.mark.get_booking_ids
def test_get_booking_ids_by_non_existing_lastname(api_client):
    params = {'lastname': 'Rorin'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)

    err_msg = f'Response body is not empty - {ids_resp.json()}'
    assert ids_resp.json() == [], err_msg


@pytest.mark.get_booking_ids
def test_get_booking_ids_by_non_existing_checkin(api_client):
    params = {'checkin': '3000-08-05'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)

    err_msg = f'Response body is not empty - {ids_resp.json()}'
    assert ids_resp.json() == [], err_msg


@pytest.mark.get_booking_ids
def test_get_booking_ids_by_non_existing_checkout(api_client):
    params = {'checkout': '3000-08-05'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)
    
    # logical error - method should return only bookings with checkout >= '2023-11-12', but it returns also <
    err_msg = f'Response body is not empty - \n{ids_resp.json()}'
    assert ids_resp.json() == [], err_msg
