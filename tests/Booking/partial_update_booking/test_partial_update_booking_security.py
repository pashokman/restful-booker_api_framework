import pytest

from data.endpoints import AUTH_ENDPOINT, CREATE_BOOKING_ENDPOINT, PARTIAL_UPDATE_BOOKING_ENDPOINT, DELETE_BOOKING_ENDPOINT
from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA


@pytest.fixture
def prepare(api_client):
    auth = api_client.post(AUTH_ENDPOINT, AUTH_DATA)
    token = auth.json()['token']
    headers = {'Cookie': f'token={token}'}

    create_booking = api_client.post(CREATE_BOOKING_ENDPOINT, NEW_BOOKING_DATA)
    booking_id = create_booking.json()['bookingid']

    yield token, booking_id, api_client

    api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id), headers=headers)


@pytest.mark.partial_update_booking
@pytest.mark.security
def test_partial_update_booking_token_and_1_symbol(prepare):
    token, booking_id, api_client = prepare
    headers = {'Cookie': f'token={token}w'}
    
    part_upd_booking = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), {'firstname': 'Joey'}, headers)

    err_msg = f"Expected status code - 403, current status code - {part_upd_booking.status_code}"
    assert part_upd_booking.status_code == 403, err_msg


@pytest.mark.partial_update_booking
@pytest.mark.security
def test_partial_update_booking_token_without_last_symbol(prepare):
    token, booking_id, api_client = prepare
    headers = {'Cookie': f'token={token[:-1]}'}
    
    part_upd_booking = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), {'firstname': 'Joey'}, headers)

    err_msg = f"Expected status code - 403, current status code - {part_upd_booking.status_code}"
    assert part_upd_booking.status_code == 403, err_msg


@pytest.mark.partial_update_booking
@pytest.mark.security
def test_partial_update_booking_token_without_first_symbol(prepare):
    token, booking_id, api_client = prepare
    headers = {'Cookie': f'token={token[1:]}'}
    
    part_upd_booking = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), {'firstname': 'Joey'}, headers)

    err_msg = f"Expected status code - 403, current status code - {part_upd_booking.status_code}"
    assert part_upd_booking.status_code == 403, err_msg


@pytest.mark.partial_update_booking
@pytest.mark.security
def test_partial_update_booking_without_token(prepare):
    token, booking_id, api_client = prepare
    headers = {'Cookie': f'token='}
    
    part_upd_booking = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), {'firstname': 'Joey'}, headers)

    err_msg = f"Expected status code - 403, current status code - {part_upd_booking.status_code}"
    assert part_upd_booking.status_code == 403, err_msg


@pytest.mark.partial_update_booking
@pytest.mark.security
def test_partial_update_booking_without_headers(prepare):
    token, booking_id, api_client = prepare
    
    part_upd_booking = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), {'firstname': 'Joey'})

    err_msg = f"Expected status code - 403, current status code - {part_upd_booking.status_code}"
    assert part_upd_booking.status_code == 403, err_msg
