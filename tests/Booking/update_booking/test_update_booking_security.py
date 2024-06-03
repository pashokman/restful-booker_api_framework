import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA, UPDATE_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import *

from utils.assertions.assert_status_code import assert_status_code


@pytest.fixture
def prepare():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json['bookingid']

    yield token, booking_id

    delete_booking(booking_id, token)


@pytest.mark.update_booking
@pytest.mark.security
def test_update_booking_token_plus_1_end_symbol(prepare):
    token, booking_id = prepare
    token = token + 'w'
    
    update_resp = update_booking(booking_id, UPDATE_BOOKING_DATA, token)
    assert_status_code(update_resp.status_code, 403)


@pytest.mark.update_booking
@pytest.mark.security
def test_update_booking_token_without_last_symbol(prepare):
    token, booking_id = prepare
    token = token[0:-1]
    
    update_resp = update_booking(booking_id, UPDATE_BOOKING_DATA, token)
    assert_status_code(update_resp.status_code, 403)


@pytest.mark.update_booking
@pytest.mark.security
def test_update_booking_token_without_first_symbol(prepare):
    token, booking_id = prepare
    token = token[1:]
    
    update_resp = update_booking(booking_id, UPDATE_BOOKING_DATA, token)
    assert_status_code(update_resp.status_code, 403)


@pytest.mark.update_booking
@pytest.mark.security
def test_update_booking_with_empty_token(prepare):
    token, booking_id = prepare
    token = ''
    
    update_resp = update_booking(booking_id, UPDATE_BOOKING_DATA, token)
    assert_status_code(update_resp.status_code, 403)


@pytest.mark.update_booking
@pytest.mark.security
def test_update_booking_without_headers(prepare):
    token, booking_id = prepare
    
    update_resp = api_client.put(UPDATE_BOOKING_ENDPOINT(booking_id), UPDATE_BOOKING_DATA)
    assert_status_code(update_resp.status_code, 403)
