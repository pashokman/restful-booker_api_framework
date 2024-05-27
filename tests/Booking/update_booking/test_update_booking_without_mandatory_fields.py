import copy
import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA, UPDATE_BOOKING_DATA
from data.endpoints import AUTH_ENDPOINT, CREATE_BOOKING_ENDPOINT, UPDATE_BOOKING_ENDPOINT, DELETE_BOOKING_ENDPOINT


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
def test_update_booking_without_firstname(preparation):
    api_client, booking_id, headers, changed_data = preparation   
    del changed_data['firstname']

    update_booking = api_client.put(UPDATE_BOOKING_ENDPOINT(booking_id), changed_data, headers)
    err_msg = f'Expected status code - 400, current status code - {update_booking.status_code}'
    assert update_booking.status_code == 400, err_msg


@pytest.mark.update_booking
def test_update_booking_without_lastname(preparation):
    api_client, booking_id, headers, changed_data = preparation
    del changed_data['lastname']

    update_booking = api_client.put(UPDATE_BOOKING_ENDPOINT(booking_id), changed_data, headers)
    err_msg = f'Expected status code - 400, current status code - {update_booking.status_code}'
    assert update_booking.status_code == 400, err_msg


@pytest.mark.update_booking
def test_update_booking_without_totalprice(preparation):
    api_client, booking_id, headers, changed_data = preparation
    del changed_data['totalprice']

    update_booking = api_client.put(UPDATE_BOOKING_ENDPOINT(booking_id), changed_data, headers)
    err_msg = f'Expected status code - 400, current status code - {update_booking.status_code}'
    assert update_booking.status_code == 400, err_msg


@pytest.mark.update_booking
def test_update_booking_without_depositpaid(preparation):
    api_client, booking_id, headers, changed_data = preparation
    del changed_data['depositpaid']

    update_booking = api_client.put(UPDATE_BOOKING_ENDPOINT(booking_id), changed_data, headers)
    err_msg = f'Expected status code - 400, current status code - {update_booking.status_code}'
    assert update_booking.status_code == 400, err_msg


@pytest.mark.update_booking
def test_update_booking_without_bookingdates(preparation):
    api_client, booking_id, headers, changed_data = preparation
    del changed_data['bookingdates']

    update_booking = api_client.put(UPDATE_BOOKING_ENDPOINT(booking_id), changed_data, headers)
    err_msg = f'Expected status code - 400, current status code - {update_booking.status_code}'
    assert update_booking.status_code == 400, err_msg


@pytest.mark.update_booking
def test_update_booking_without_bookingdates_checkin(preparation):
    api_client, booking_id, headers, changed_data = preparation
    del changed_data['bookingdates']['checkin']

    update_booking = api_client.put(UPDATE_BOOKING_ENDPOINT(booking_id), changed_data, headers)
    err_msg = f'Expected status code - 400, current status code - {update_booking.status_code}'
    assert update_booking.status_code == 400, err_msg


@pytest.mark.update_booking
def test_update_booking_without_bookingdates_checkout(preparation):
    api_client, booking_id, headers, changed_data = preparation
    del changed_data['bookingdates']['checkout']

    update_booking = api_client.put(UPDATE_BOOKING_ENDPOINT(booking_id), changed_data, headers)
    err_msg = f'Expected status code - 400, current status code - {update_booking.status_code}'
    assert update_booking.status_code == 400, err_msg
