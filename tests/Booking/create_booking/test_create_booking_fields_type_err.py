import copy
import pytest

from data.endpoints import CREATE_BOOKING_ENDPOINT
from data.booking.booking_objects import NEW_BOOKING_DATA


@pytest.mark.create_booking
def test_create_booking_firstname_not_string(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['firstname'] = 123

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code

    exp_status_code = 500
    err_msg = f'Expected status code - {exp_status_code}, current status code - {resp_status}'
    assert resp_status == exp_status_code, err_msg


@pytest.mark.create_booking
def test_create_booking_lastname_not_string(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['lastname'] = 123

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code

    exp_status_code = 500
    err_msg = f'Expected status code - {exp_status_code}, current status code - {resp_status}'
    assert resp_status == exp_status_code, err_msg


@pytest.mark.create_booking
def test_create_booking_totalprice_not_number(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['totalprice'] = 'price'

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code

    exp_status_code = 500
    err_msg = f'Expected status code - {exp_status_code}, current status code - {resp_status}'
    assert resp_status == exp_status_code, err_msg


@pytest.mark.create_booking
def test_create_booking_depositpaid_not_boolean(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['depositpaid'] = 'deposit'

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code

    exp_status_code = 500
    err_msg = f'Expected status code - {exp_status_code}, current status code - {resp_status}'
    assert resp_status == exp_status_code, err_msg


@pytest.mark.create_booking
def test_create_booking_bookingdates_not_dictionary(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['bookingdates'] = 'some string'

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code

    exp_status_code = 500
    err_msg = f'Expected status code - {exp_status_code}, current status code - {resp_status}'
    assert resp_status == exp_status_code, err_msg


@pytest.mark.create_booking
def test_create_booking_bookingdates_checkin_not_date(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['bookingdates']['checkin'] = 321

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code

    exp_status_code = 500
    err_msg = f'Expected status code - {exp_status_code}, current status code - {resp_status}'
    assert resp_status == exp_status_code, err_msg


@pytest.mark.create_booking
def test_create_booking_bookingdates_checkout_not_date(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['bookingdates']['checkout'] = 321

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code

    exp_status_code = 500
    err_msg = f'Expected status code - {exp_status_code}, current status code - {resp_status}'
    assert resp_status == exp_status_code, err_msg


@pytest.mark.create_booking
def test_create_booking_additionalneeds_not_string(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    changed_data['additionalneeds'] = 321

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code

    exp_status_code = 500
    err_msg = f'Expected status code - {exp_status_code}, current status code - {resp_status}'
    assert resp_status == exp_status_code, err_msg