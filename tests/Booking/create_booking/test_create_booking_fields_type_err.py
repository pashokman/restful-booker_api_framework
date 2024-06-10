import copy
import pytest

from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.booking import create_booking

from utils.assertions.assert_status_code import assert_status_code


@pytest.mark.create_booking
def test_create_booking_firstname_not_string():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['firstname'] = 123

    response = create_booking(changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_lastname_not_string():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['lastname'] = 123

    response = create_booking(changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_totalprice_not_number():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    # totalprice should be integer
    changed_data['totalprice'] = 'price'

    response = create_booking(changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_totalprice_not_integer():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    # totalprice should be integer
    changed_data['totalprice'] = 123.45

    response = create_booking(changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_depositpaid_not_boolean():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    # depositpaid should be boolean
    changed_data['depositpaid'] = 'deposit'

    response = create_booking(changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_bookingdates_not_dictionary():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['bookingdates'] = 'some string'

    response = create_booking(changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_bookingdates_checkin_not_string_date():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    # bookingdates-checkin should be date string
    changed_data['bookingdates']['checkin'] = 321

    response = create_booking(changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_bookingdates_checkout_not_string_date():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    # bookingdates-checkout should be date string
    changed_data['bookingdates']['checkout'] = 321

    response = create_booking(changed_data)
    assert_status_code(response.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_additionalneeds_not_string():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    # additionalneeds should be string
    changed_data['additionalneeds'] = 321

    response = create_booking(changed_data)
    assert_status_code(response.status_code, 500)