import copy
import pytest

from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.booking import *

from utils.assertions.assert_status_code import assert_status_code


@pytest.mark.create_booking
def test_create_booking_without_firstname():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data.pop('firstname', 'Key not exist')

    create_resp = create_booking(changed_data)

    assert_status_code(create_resp.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_without_lastname():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data.pop('lastname', 'Key not exist')

    create_resp = create_booking(changed_data)

    assert_status_code(create_resp.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_without_totalprice():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data.pop('totalprice', 'Key not exist')

    create_resp = create_booking(changed_data)

    assert_status_code(create_resp.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_without_depositpaid():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data.pop('depositpaid', 'Key not exist')

    create_resp = create_booking(changed_data)

    assert_status_code(create_resp.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_without_bookingdates():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data.pop('bookingdates', 'Key not exist')

    create_resp = create_booking(changed_data)

    assert_status_code(create_resp.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_without_bookingdates_checkin():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data.get('bookingdates', 'Key not exist').pop('checkin', 'Key not exist')

    create_resp = create_booking(changed_data)

    assert_status_code(create_resp.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_without_bookingdates_checkout():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data.get('bookingdates', 'Key not exist').pop('checkout', 'Key not exist')

    create_resp = create_booking(changed_data)

    assert_status_code(create_resp.status_code, 500)