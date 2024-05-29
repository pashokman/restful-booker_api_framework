import copy
import pytest

from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.booking import *

from utils.assertions.assert_status_code import assert_status_code


@pytest.mark.create_booking
def test_create_booking_firstname_not_string(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['firstname'] = 123

    response = create_booking(api_client, changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_lastname_not_string(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['lastname'] = 123

    response = create_booking(api_client, changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_totalprice_not_number(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['totalprice'] = 'price'

    response = create_booking(api_client, changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_totalprice_not_integer(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['totalprice'] = 123.45

    response = create_booking(api_client, changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_depositpaid_not_boolean(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['depositpaid'] = 'deposit'

    response = create_booking(api_client, changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_bookingdates_not_dictionary(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['bookingdates'] = 'some string'

    response = create_booking(api_client, changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_bookingdates_checkin_not_date(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['bookingdates']['checkin'] = 321

    response = create_booking(api_client, changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_bookingdates_checkout_not_date(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['bookingdates']['checkout'] = 321

    response = create_booking(api_client, changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_additionalneeds_not_string(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['additionalneeds'] = 321

    response = create_booking(api_client, changed_data)
    assert_status_code(response.status_code, 500)