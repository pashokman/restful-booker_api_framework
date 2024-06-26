import copy
import pytest

from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.booking import create_booking

from utils.assertions.assert_status_code import assert_status_code


pytestmark = pytest.mark.create_booking


def test_create_booking_totalprice_0():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    # totalprice can't be 0
    changed_data['totalprice'] = 0

    response = create_booking(changed_data)
    assert_status_code(response.status_code, 403)


def test_create_booking_totalprice_less_than_0():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    # totalprice can't be < 0
    changed_data['totalprice'] = -500

    response = create_booking(changed_data)
    assert_status_code(response.status_code, 403)


def test_create_booking_bookingdates_checkout_before_checkin():
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    new_checkin = changed_data.get('bookingdates', 'Key not exist').get('checkout', 'Key not exist')
    new_checkout = changed_data.get('bookingdates', 'Key not exist').get('checkin', 'Key not exist')
    # chekout can't be < checkin
    changed_data['bookingdates']['checkin'] = new_checkin
    changed_data['bookingdates']['checkout'] = new_checkout

    response = create_booking(changed_data)
    assert_status_code(response.status_code, 403)
