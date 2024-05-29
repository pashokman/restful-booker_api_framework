import copy
import pytest

from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.booking import *

from utils.assertions.assert_status_code import assert_status_code


@pytest.mark.create_booking
def test_create_booking_totalprice_0(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['totalprice'] = 0

    response = create_booking(api_client, changed_data)
    assert_status_code(response.status_code, 403)


@pytest.mark.create_booking
def test_create_booking_totalprice_less_than_0(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['totalprice'] = -500

    response = create_booking(api_client, changed_data)
    assert_status_code(response.status_code, 403)


@pytest.mark.create_booking
def test_create_booking_bookingdates_checkout_before_checkin(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    new_checkin = changed_data['bookingdates']['checkout']
    new_checkout = changed_data['bookingdates']['checkin']
    changed_data['bookingdates']['checkin'] = new_checkin
    changed_data['bookingdates']['checkout'] = new_checkout

    response = create_booking(api_client, changed_data)
    assert_status_code(response.status_code, 403)
