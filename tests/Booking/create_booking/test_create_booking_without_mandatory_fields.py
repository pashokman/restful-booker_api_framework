import pytest
import copy
from data.endpoints import CREATE_BOOKING_ENDPOINT
from data.booking.booking_objects import NEW_BOOKING_DATA


@pytest.mark.create_booking
def test_create_booking_without_firstname(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['firstname']

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code
    exp_status = 500
    err_msg = f'Expected status code - {exp_status}. Current status code - {resp_status}'
    assert resp_status == 500, err_msg


@pytest.mark.create_booking
def test_create_booking_without_lastname(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['lastname']

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code
    exp_status = 500
    err_msg = f'Expected status code - {exp_status}. Current status code - {resp_status}'
    assert resp_status == 500, err_msg


@pytest.mark.create_booking
def test_create_booking_without_totalprice(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['totalprice']

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code
    exp_status = 500
    err_msg = f'Expected status code - {exp_status}. Current status code - {resp_status}'
    assert resp_status == 500, err_msg


@pytest.mark.create_booking
def test_create_booking_without_depositpaid(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['depositpaid']

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code
    exp_status = 500
    err_msg = f'Expected status code - {exp_status}. Current status code - {resp_status}'
    assert resp_status == 500, err_msg


@pytest.mark.create_booking
def test_create_booking_without_bookingdates(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['bookingdates']

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code
    exp_status = 500
    err_msg = f'Expected status code - {exp_status}. Current status code - {resp_status}'
    assert resp_status == 500, err_msg


@pytest.mark.create_booking
def test_create_booking_without_bookingdates_checkin(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['bookingdates']['checkin']

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code
    exp_status = 500
    err_msg = f'Expected status code - {exp_status}. Current status code - {resp_status}'
    assert resp_status == 500, err_msg


@pytest.mark.create_booking
def test_create_booking_without_bookingdates_checkout(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['bookingdates']['checkout']

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_status = response.status_code
    exp_status = 500
    err_msg = f'Expected status code - {exp_status}. Current status code - {resp_status}'
    assert resp_status == 500, err_msg