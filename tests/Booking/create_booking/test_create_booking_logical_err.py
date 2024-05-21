import pytest
import copy
from data.endpoints import CREATE_BOOKING_ENDPOINT
from data.booking.booking_objects import NEW_BOOKING_DATA


@pytest.mark.create_booking
def test_create_booking_totalprice_0(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['totalprice'] = 0

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code

    exp_status_code = 403
    err_msg = f'Expected status code - {exp_status_code}, current status code - {resp_status}'
    assert resp_status == exp_status_code, err_msg


@pytest.mark.create_booking
def test_create_booking_totalprice_less_than_0(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['totalprice'] = -500.13

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code

    exp_status_code = 403
    err_msg = f'Expected status code - {exp_status_code}, current status code - {resp_status}'
    assert resp_status == exp_status_code, err_msg


@pytest.mark.create_booking
def test_create_booking_bookingdates_checkout_before_checkin(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    new_checkin = changed_data['bookingdates']['checkout']
    new_checkout = changed_data['bookingdates']['checkin']
    changed_data['bookingdates']['checkin'] = new_checkin
    changed_data['bookingdates']['checkout'] = new_checkout

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code

    exp_status_code = 403
    err_msg = f'Expected status code - {exp_status_code}, current status code - {resp_status}'
    assert resp_status == exp_status_code, err_msg
