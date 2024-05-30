import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA, NEW_BOOKING_DATA2

from utils.methods.authorization import authorization
from utils.methods.booking import *

from utils.assertions.assert_status_code import assert_status_code
from utils.assertions.assert_obj_in_obj import assert_obj_in_obj
from utils.assertions.assert_obj_not_in_obj import assert_obj_not_in_obj


@pytest.fixture()
def three_bookings_creation():
    token = authorization(AUTH_DATA)

    # create 2 same books and one different
    first_booking_resp = create_booking(NEW_BOOKING_DATA)
    first_id = first_booking_resp.json()['bookingid']

    second_booking_resp = create_booking(NEW_BOOKING_DATA)
    second_id = second_booking_resp.json()['bookingid']

    third_booking_resp = create_booking(NEW_BOOKING_DATA2)
    third_id = third_booking_resp.json()['bookingid']

    yield first_id, second_id, third_id

    delete_booking(first_id, token)
    delete_booking(second_id, token)
    delete_booking(third_id, token)


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_firstname_lastname_success(three_bookings_creation):
    first_id, second_id, third_id = three_bookings_creation

    params = {'firstname': 'Lester', 'lastname': 'Tester'}
    get_ids_resp = get_booking_ids(params)
    get_ids_resp_json = get_ids_resp.json()

    assert_status_code(get_ids_resp.status_code, 200)
    assert_obj_in_obj({'bookingid': first_id}, get_ids_resp_json)
    assert_obj_in_obj({'bookingid': second_id}, get_ids_resp_json)
    assert_obj_not_in_obj({'bookingid': third_id}, get_ids_resp_json)


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_firstname_success(three_bookings_creation):
    first_id, second_id, third_id = three_bookings_creation

    params = {'firstname': 'Lester'}
    get_ids_resp = get_booking_ids(params)
    get_ids_resp_json = get_ids_resp.json()

    assert_status_code(get_ids_resp.status_code, 200)
    assert_obj_in_obj({'bookingid': first_id}, get_ids_resp_json)
    assert_obj_in_obj({'bookingid': second_id}, get_ids_resp_json)
    assert_obj_not_in_obj({'bookingid': third_id}, get_ids_resp_json)


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_lastname_success(three_bookings_creation):
    first_id, second_id, third_id = three_bookings_creation

    params = {'lastname': 'Tester'}
    get_ids_resp = get_booking_ids(params)
    get_ids_resp_json = get_ids_resp.json()

    assert_status_code(get_ids_resp.status_code, 200)
    assert_obj_in_obj({'bookingid': first_id}, get_ids_resp_json)
    assert_obj_in_obj({'bookingid': second_id}, get_ids_resp_json)
    assert_obj_not_in_obj({'bookingid': third_id}, get_ids_resp_json)


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_checkin_success(three_bookings_creation):
    first_id, second_id, third_id = three_bookings_creation

    params = {'checkin': '2023-11-11'}
    get_ids_resp = get_booking_ids(params)
    get_ids_resp_json = get_ids_resp.json()

    assert_status_code(get_ids_resp.status_code, 200)
    # logical errors - method should return bookings with checkin >= '2023-11-11', but it returns only >
    assert_obj_in_obj({'bookingid': first_id}, get_ids_resp_json)
    assert_obj_in_obj({'bookingid': second_id}, get_ids_resp_json)
    assert_obj_not_in_obj({'bookingid': third_id}, get_ids_resp_json)


@pytest.mark.get_booking_ids
@pytest.mark.success
def test_get_booking_ids_by_checkout_success(three_bookings_creation):
    first_id, second_id, third_id = three_bookings_creation

    params = {'checkout': '2023-11-12'}
    get_ids_resp = get_booking_ids(params)
    get_ids_resp_json = get_ids_resp.json()

    assert_status_code(get_ids_resp.status_code, 200)
    assert_obj_in_obj({'bookingid': first_id}, get_ids_resp_json)
    assert_obj_in_obj({'bookingid': second_id}, get_ids_resp_json)
    # logical error - method should return only bookings with checkout >= '2023-11-12', but it returns also <
    assert_obj_not_in_obj({'bookingid': third_id}, get_ids_resp_json)
