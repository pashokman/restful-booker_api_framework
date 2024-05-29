import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import *

from utils.assertions.assert_status_code import assert_status_code


@pytest.fixture
def prepare(api_client):
    token = authorization(api_client, AUTH_DATA)

    create_resp = create_booking(api_client, NEW_BOOKING_DATA)
    booking_id = create_resp.json()['bookingid']

    yield token, booking_id, api_client

    delete_booking(api_client, booking_id, token)


@pytest.mark.delete_booking
@pytest.mark.security
def test_delete_booking_token_and_1_symbol(prepare):
    token, booking_id, api_client = prepare
    headers = {'Cookie': f'token={token}w'}

    del_booking = api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id), headers=headers)

    assert_status_code(del_booking.status_code, 403)


@pytest.mark.delete_booking
@pytest.mark.security
def test_delete_booking_token_without_last_symbol(prepare):
    token, booking_id, api_client = prepare
    headers = {'Cookie': f'token={token[:-1]}'}

    del_booking = api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id), headers=headers)

    assert_status_code(del_booking.status_code, 403)


@pytest.mark.delete_booking
@pytest.mark.security
def test_delete_booking_token_without_first_symbol(prepare):
    token, booking_id, api_client = prepare
    headers = {'Cookie': f'token={token[1:]}'}

    del_booking = api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id), headers=headers)

    assert_status_code(del_booking.status_code, 403)


@pytest.mark.delete_booking
@pytest.mark.security
def test_delete_booking_without_token(prepare):
    token, booking_id, api_client = prepare
    headers = {'Cookie': f'token='}

    del_booking = api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id), headers=headers)

    assert_status_code(del_booking.status_code, 403)


@pytest.mark.delete_booking
@pytest.mark.security
def test_delete_booking_without_headers(prepare):
    token, booking_id, api_client = prepare

    del_booking = api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id))

    assert_status_code(del_booking.status_code, 403)