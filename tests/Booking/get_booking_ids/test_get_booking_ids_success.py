import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA, NEW_BOOKING_DATA2
from data.endpoints import AUTH_ENDPOINT, CREATE_BOOKING_ENDPOINT, GET_BOOKING_IDS_ENDPOINT, DELETE_BOOKING_ENDPOINT


@pytest.fixture()
def three_bookings_creation(api_client):
    auth = api_client.post(AUTH_ENDPOINT, AUTH_DATA)
    token = auth.json()['token']
    headers = {'Cookie': f'token={token}'}

    # create 2 same books and one different
    first_booking_resp = api_client.post(CREATE_BOOKING_ENDPOINT, NEW_BOOKING_DATA)
    first_id = first_booking_resp.json()['bookingid']

    second_booking_resp = api_client.post(CREATE_BOOKING_ENDPOINT, NEW_BOOKING_DATA)
    second_id = second_booking_resp.json()['bookingid']

    third_booking_resp = api_client.post(CREATE_BOOKING_ENDPOINT, NEW_BOOKING_DATA2)
    third_id = third_booking_resp.json()['bookingid']

    yield api_client, first_id, second_id, third_id

    api_client.delete(DELETE_BOOKING_ENDPOINT(first_id), headers=headers)
    api_client.delete(DELETE_BOOKING_ENDPOINT(second_id), headers=headers)
    api_client.delete(DELETE_BOOKING_ENDPOINT(third_id), headers=headers)


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_firstname_lastname_success(three_bookings_creation):
    api_client, first_id, second_id, third_id = three_bookings_creation

    params = {'firstname': 'Lester', 'lastname': 'Tester'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)

    status_err_msg = f'Expected status code - 200, current status code - {ids_resp.status_code}'
    assert ids_resp.status_code == 200, status_err_msg
    first_id_err_msg = f'First id - {first_id} is not in response body'
    assert {'bookingid': first_id} in ids_resp.json(), first_id_err_msg
    second_id_err_msg = f'Second id - {second_id} is not in response body'
    assert {'bookingid': second_id} in ids_resp.json(), second_id_err_msg
    third_id_err_msg = f'Third id - {third_id} is in response body'
    assert {'bookingid': third_id} not in ids_resp.json(), third_id_err_msg


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_firstname_success(three_bookings_creation):
    api_client, first_id, second_id, third_id = three_bookings_creation

    params = {'firstname': 'Lester'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)

    status_err_msg = f'Expected status code - 200, current status code - {ids_resp.status_code}'
    assert ids_resp.status_code == 200, status_err_msg
    first_id_err_msg = f'First id - {first_id} is not in response body'
    assert {'bookingid': first_id} in ids_resp.json(), first_id_err_msg
    second_id_err_msg = f'Second id - {second_id} is not in response body'
    assert {'bookingid': second_id} in ids_resp.json(), second_id_err_msg
    third_id_err_msg = f'Third id - {third_id} is in response body'
    assert {'bookingid': third_id} not in ids_resp.json(), third_id_err_msg


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_lastname_success(three_bookings_creation):
    api_client, first_id, second_id, third_id = three_bookings_creation

    params = {'lastname': 'Tester'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)

    status_err_msg = f'Expected status code - 200, current status code - {ids_resp.status_code}'
    assert ids_resp.status_code == 200, status_err_msg
    first_id_err_msg = f'First id - {first_id} is not in response body'
    assert {'bookingid': first_id} in ids_resp.json(), first_id_err_msg
    second_id_err_msg = f'Second id - {second_id} is not in response body'
    assert {'bookingid': second_id} in ids_resp.json(), second_id_err_msg
    third_id_err_msg = f'Third id - {third_id} is in response body'
    assert {'bookingid': third_id} not in ids_resp.json(), third_id_err_msg


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_checkin_success(three_bookings_creation):
    api_client, first_id, second_id, third_id = three_bookings_creation

    params = {'checkin': '2023-11-11'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)

    status_err_msg = f'Expected status code - 200, current status code - {ids_resp.status_code}' 
    assert ids_resp.status_code == 200, status_err_msg
    # logical errors - method should return bookings with checkin >= '2023-11-11', but it returns only >
    first_id_err_msg = f'First id - {first_id} is not in response body'
    assert {'bookingid': first_id} in ids_resp.json(), first_id_err_msg
    second_id_err_msg = f'Second id - {second_id} is not in response body'
    assert {'bookingid': second_id} in ids_resp.json(), second_id_err_msg
    third_id_err_msg = f'Third id - {third_id} is in response body'
    assert {'bookingid': third_id} not in ids_resp.json(), third_id_err_msg


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_checkout_success(three_bookings_creation):
    api_client, first_id, second_id, third_id = three_bookings_creation

    params = {'checkout': '2023-11-12'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)

    status_err_msg = f'Expected status code - 200, current status code - {ids_resp.status_code}' 
    assert ids_resp.status_code == 200, status_err_msg 
    first_id_err_msg = f'First id - {first_id} is not in response body'
    assert {'bookingid': first_id} in ids_resp.json(), first_id_err_msg
    second_id_err_msg = f'Second id - {second_id} is not in response body'
    assert {'bookingid': second_id} in ids_resp.json(), second_id_err_msg
    # logical error - method should return only bookings with checkout >= '2023-11-12', but it returns also <
    third_id_err_msg = f'Third id - {third_id} is in response body'
    assert {'bookingid': third_id} not in ids_resp.json(), third_id_err_msg
