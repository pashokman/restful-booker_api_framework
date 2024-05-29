import copy
import pytest

from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.booking import *

from utils.assertions.assert_status_code import assert_status_code


@pytest.mark.create_booking
def test_create_booking_without_firstname(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['firstname']

    create_resp = create_booking(api_client, changed_data)

    assert_status_code(create_resp.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_without_lastname(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['lastname']

    create_resp = create_booking(api_client, changed_data)

    assert_status_code(create_resp.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_without_totalprice(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['totalprice']

    create_resp = create_booking(api_client, changed_data)

    assert_status_code(create_resp.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_without_depositpaid(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['depositpaid']

    create_resp = create_booking(api_client, changed_data)

    assert_status_code(create_resp.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_without_bookingdates(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['bookingdates']

    create_resp = create_booking(api_client, changed_data)

    assert_status_code(create_resp.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_without_bookingdates_checkin(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['bookingdates']['checkin']

    create_resp = create_booking(api_client, changed_data)

    assert_status_code(create_resp.status_code, 500)


@pytest.mark.create_booking
def test_create_booking_without_bookingdates_checkout(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['bookingdates']['checkout']

    create_resp = create_booking(api_client, changed_data)

    assert_status_code(create_resp.status_code, 500)