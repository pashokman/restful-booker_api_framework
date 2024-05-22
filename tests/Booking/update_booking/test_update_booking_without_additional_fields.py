import copy
import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA, UPDATE_BOOKING_DATA
from data.endpoints import AUTH_ENDPOINT, CREATE_BOOKING_ENDPOINT, GET_BOOKING_ENDPOINT, UPDATE_BOOKING_ENDPOINT, DELETE_BOOKING_ENDPOINT


@pytest.fixture
def preparation(api_client):
    auth = api_client.post(AUTH_ENDPOINT, AUTH_DATA)
    token = auth.json()['token']

    new_booking = api_client.post(CREATE_BOOKING_ENDPOINT, NEW_BOOKING_DATA)
    booking_id = new_booking.json()['bookingid']

    headers = {'Cookie': f'token={token}'}
    changed_data = copy.deepcopy(UPDATE_BOOKING_DATA)

    yield api_client, booking_id, headers, changed_data

    api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id), headers=headers)


@pytest.mark.update_booking
@pytest.mark.success
def test_update_booking_without_additionalneeds(preparation):
    api_client, booking_id, headers, changed_data = preparation
    del changed_data['additionalneeds']

    exp_obj = UPDATE_BOOKING_DATA
    exp_obj['additionalneeds'] = NEW_BOOKING_DATA['additionalneeds']
    
    update_booking = api_client.put(UPDATE_BOOKING_ENDPOINT(booking_id), changed_data, headers=headers)
    get_booking = api_client.get(GET_BOOKING_ENDPOINT(booking_id))

    status_err_msg = f'Expected status code - 200, current status code - {update_booking.status_code}'
    assert update_booking.status_code == 200, status_err_msg
    update_body_err_msg = f'Expected body - \n{UPDATE_BOOKING_DATA}, \ncurrent body - \n{update_booking.json()}'
    assert update_booking.json() == exp_obj, update_body_err_msg
    get_body_err_msg = f'Expected body - \n{UPDATE_BOOKING_DATA}, \ncurrent body - \n{get_booking.json()}'
    assert get_booking.json() == UPDATE_BOOKING_DATA, get_body_err_msg