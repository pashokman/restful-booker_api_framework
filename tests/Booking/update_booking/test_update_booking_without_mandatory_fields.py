import copy
import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA, UPDATE_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import *

from utils.assertions.assert_status_code import assert_status_code


@pytest.fixture
def preparation():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json['bookingid']

    changed_data = copy.deepcopy(UPDATE_BOOKING_DATA)

    yield token, booking_id, changed_data

    delete_booking(booking_id, token)


@pytest.mark.update_booking
def test_update_booking_without_firstname(preparation):
    token, booking_id, changed_data = preparation   
    del changed_data['firstname']

    update_resp = update_booking(booking_id, changed_data, token)
    assert_status_code(update_resp.status_code, 400)


@pytest.mark.update_booking
def test_update_booking_without_lastname(preparation):
    token, booking_id, changed_data = preparation
    del changed_data['lastname']

    update_resp = update_booking(booking_id, changed_data, token)
    assert_status_code(update_resp.status_code, 400)


@pytest.mark.update_booking
def test_update_booking_without_totalprice(preparation):
    token, booking_id, changed_data = preparation
    del changed_data['totalprice']

    update_resp = update_booking(booking_id, changed_data, token)
    assert_status_code(update_resp.status_code, 400)


@pytest.mark.update_booking
def test_update_booking_without_depositpaid(preparation):
    token, booking_id, changed_data = preparation
    del changed_data['depositpaid']

    update_resp = update_booking(booking_id, changed_data, token)
    assert_status_code(update_resp.status_code, 400)


@pytest.mark.update_booking
def test_update_booking_without_bookingdates(preparation):
    token, booking_id, changed_data = preparation
    del changed_data['bookingdates']

    update_resp = update_booking(booking_id, changed_data, token)
    assert_status_code(update_resp.status_code, 400)


@pytest.mark.update_booking
def test_update_booking_without_bookingdates_checkin(preparation):
    token, booking_id, changed_data = preparation
    del changed_data['bookingdates']['checkin']

    update_resp = update_booking(booking_id, changed_data, token)
    assert_status_code(update_resp.status_code, 400)


@pytest.mark.update_booking
def test_update_booking_without_bookingdates_checkout(preparation):
    token, booking_id, changed_data = preparation
    del changed_data['bookingdates']['checkout']

    update_resp = update_booking(booking_id, changed_data, token)
    assert_status_code(update_resp.status_code, 400)
