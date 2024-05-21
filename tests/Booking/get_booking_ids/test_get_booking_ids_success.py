import pytest
from data.booking.booking_objects import NEW_BOOKING_DATA, NEW_BOOKING_DATA2
from data.endpoints import CREATE_BOOKING_ENDPOINT, GET_BOOKING_IDS_ENDPOINT


@pytest.fixture()
def three_bookings_creation(api_client):
    # create 2 same books and one different
    first_booking_resp = api_client.post(CREATE_BOOKING_ENDPOINT, NEW_BOOKING_DATA)
    first_id = first_booking_resp.json()['bookingid']

    second_booking_resp = api_client.post(CREATE_BOOKING_ENDPOINT, NEW_BOOKING_DATA)
    second_id = second_booking_resp.json()['bookingid']

    third_booking_resp = api_client.post(CREATE_BOOKING_ENDPOINT, NEW_BOOKING_DATA2)
    third_id = third_booking_resp.json()['bookingid']

    return first_id, second_id, third_id


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_firstname_lastname_success(api_client, three_bookings_creation):
    first_id, second_id, third_id = three_bookings_creation

    params = {'firstname': 'Lester', 'lastname': 'Tester'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)

    assert ids_resp.status_code == 200
    assert {'bookingid': first_id} in ids_resp.json()
    assert {'bookingid': second_id} in ids_resp.json()
    assert {'bookingid': third_id} not in ids_resp.json()


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_firstname_success(api_client, three_bookings_creation):
    first_id, second_id, third_id = three_bookings_creation

    params = {'firstname': 'Lester'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)

    assert ids_resp.status_code == 200
    assert {'bookingid': first_id} in ids_resp.json()
    assert {'bookingid': second_id} in ids_resp.json()
    assert {'bookingid': third_id} not in ids_resp.json()


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_lastname_success(api_client, three_bookings_creation):
    first_id, second_id, third_id = three_bookings_creation

    params = {'lastname': 'Tester'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)

    assert ids_resp.status_code == 200
    assert {'bookingid': first_id} in ids_resp.json()
    assert {'bookingid': second_id} in ids_resp.json()
    assert {'bookingid': third_id} not in ids_resp.json()


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_checkin_success(api_client, three_bookings_creation):
    first_id, second_id, third_id = three_bookings_creation

    params = {'checkin': '2023-11-11'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)

    assert ids_resp.status_code == 200
    # logical errors - method should return bookings with checkin >= '2023-11-11', but it returns only >
    assert {'bookingid': first_id} in ids_resp.json()
    assert {'bookingid': second_id} in ids_resp.json()
    assert {'bookingid': third_id} not in ids_resp.json()



@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_checkout_success(api_client, three_bookings_creation):
    first_id, second_id, third_id = three_bookings_creation

    params = {'checkout': '2023-11-12'}
    ids_resp = api_client.get(GET_BOOKING_IDS_ENDPOINT, params=params)

    assert ids_resp.status_code == 200
    assert {'bookingid': first_id} in ids_resp.json()
    assert {'bookingid': second_id} in ids_resp.json()
    # logical error - method should return only bookings with checkout >= '2023-11-12', but it returns also <
    assert {'bookingid': third_id} not in ids_resp.json()

