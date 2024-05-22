import copy
import pytest

from data.endpoints import *
from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA, UPDATE_BOOKING_DATA


@pytest.fixture
def prepare(api_client):
    auth = api_client.post(AUTH_ENDPOINT, AUTH_DATA)
    token = auth.json()['token']
    headers = {'Cookie': f'token={token}'}

    new_booking = api_client.post(CREATE_BOOKING_ENDPOINT, NEW_BOOKING_DATA)
    booking_id = new_booking.json()['bookingid']

    yield api_client, headers, booking_id

    api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id), headers)


@pytest.mark.partial_update_booking
@pytest.mark.success
def test_partial_update_booking_all_params_success(prepare):
    api_client, headers, booking_id = prepare

    part_update = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), UPDATE_BOOKING_DATA, headers)
    get_booking = api_client.get(GET_BOOKING_ENDPOINT(booking_id))

    status_err = f'Expected status code - 200, current status code - {part_update.status_code}'
    assert part_update.status_code == 200, status_err
    part_update_body_err = f'Expected body - \n{UPDATE_BOOKING_DATA}, \ncurrent body - \n{part_update.json()}'
    assert part_update.json() == UPDATE_BOOKING_DATA, part_update_body_err
    get_body_err = f'Expected body - \n{UPDATE_BOOKING_DATA}, \ncurrent body - \n{get_booking.json()}'
    assert get_booking.json() == UPDATE_BOOKING_DATA, get_body_err


@pytest.mark.partial_update_booking
@pytest.mark.success
def test_partial_update_booking_firstname_param_success(prepare):
    api_client, headers, booking_id = prepare

    firstname = 'Trevor'
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['firstname'] = firstname
    update_data = {'firstname': firstname}
    part_update = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), update_data, headers)
    get_booking = api_client.get(GET_BOOKING_ENDPOINT(booking_id))

    status_err = f'Expected status code - 200, current status code - {part_update.status_code}'
    assert part_update.status_code == 200, status_err
    part_update_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{part_update.json()}'
    assert part_update.json() == exp_booking, part_update_body_err
    get_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{get_booking.json()}'
    assert get_booking.json() == exp_booking, get_body_err


@pytest.mark.partial_update_booking
@pytest.mark.success
def test_partial_update_booking_lastname_param_success(prepare):
    api_client, headers, booking_id = prepare

    lastname = 'Kollins'
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['lastname'] = lastname
    update_data = {'lastname': lastname}
    part_update = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), update_data, headers)
    get_booking = api_client.get(GET_BOOKING_ENDPOINT(booking_id))

    status_err = f'Expected status code - 200, current status code - {part_update.status_code}'
    assert part_update.status_code == 200, status_err
    part_update_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{part_update.json()}'
    assert part_update.json() == exp_booking, part_update_body_err
    get_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{get_booking.json()}'
    assert get_booking.json() == exp_booking, get_body_err


@pytest.mark.partial_update_booking
@pytest.mark.success
def test_partial_update_booking_totalprice_param_success(prepare):
    api_client, headers, booking_id = prepare

    totalprice = 2345
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['totalprice'] = totalprice
    update_data = {'totalprice': totalprice}
    part_update = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), update_data, headers)
    get_booking = api_client.get(GET_BOOKING_ENDPOINT(booking_id))

    status_err = f'Expected status code - 200, current status code - {part_update.status_code}'
    assert part_update.status_code == 200, status_err
    part_update_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{part_update.json()}'
    assert part_update.json() == exp_booking, part_update_body_err
    get_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{get_booking.json()}'
    assert get_booking.json() == exp_booking, get_body_err


@pytest.mark.partial_update_booking
@pytest.mark.success
def test_partial_update_booking_depositpaid_param_success(prepare):
    api_client, headers, booking_id = prepare

    depositpaid = False
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['depositpaid'] = depositpaid
    update_data = {'depositpaid': depositpaid}
    part_update = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), update_data, headers)
    get_booking = api_client.get(GET_BOOKING_ENDPOINT(booking_id))

    status_err = f'Expected status code - 200, current status code - {part_update.status_code}'
    assert part_update.status_code == 200, status_err
    part_update_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{part_update.json()}'
    assert part_update.json() == exp_booking, part_update_body_err
    get_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{get_booking.json()}'
    assert get_booking.json() == exp_booking, get_body_err


@pytest.mark.partial_update_booking
@pytest.mark.success
def test_partial_update_booking_bookingdates_param_success(prepare):
    api_client, headers, booking_id = prepare

    bookingdates = {
        "checkin" : "2023-11-15",
        "checkout" : "2023-11-16"
    }
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['bookingdates'] = bookingdates
    update_data = {'bookingdates': bookingdates}
    part_update = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), update_data, headers)
    get_booking = api_client.get(GET_BOOKING_ENDPOINT(booking_id))

    status_err = f'Expected status code - 200, current status code - {part_update.status_code}'
    assert part_update.status_code == 200, status_err
    part_update_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{part_update.json()}'
    assert part_update.json() == exp_booking, part_update_body_err
    get_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{get_booking.json()}'
    assert get_booking.json() == exp_booking, get_body_err


@pytest.mark.partial_update_booking
@pytest.mark.success
def test_partial_update_booking_bookingdates_checkin_param_success(prepare):
    api_client, headers, booking_id = prepare

    checkin = "2023-11-15"
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['bookingdates']['checkin'] = checkin
    exp_booking['bookingdates']['checkout'] = '0NaN-aN-aN'
    update_data = {'bookingdates':{'checkin': checkin}}
    part_update = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), update_data, headers)
    get_booking = api_client.get(GET_BOOKING_ENDPOINT(booking_id))

    status_err = f'Expected status code - 200, current status code - {part_update.status_code}'
    assert part_update.status_code == 200, status_err
    part_update_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{part_update.json()}'
    assert part_update.json() == exp_booking, part_update_body_err
    get_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{get_booking.json()}'
    assert get_booking.json() == exp_booking, get_body_err


@pytest.mark.partial_update_booking
@pytest.mark.success
def test_partial_update_booking_bookingdates_checkout_param_success(prepare):
    api_client, headers, booking_id = prepare

    checkout = "2023-11-15"
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['bookingdates']['checkin'] = '0NaN-aN-aN'
    exp_booking['bookingdates']['checkout'] = checkout
    update_data = {'bookingdates':{'checkout': checkout}}
    part_update = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), update_data, headers)
    get_booking = api_client.get(GET_BOOKING_ENDPOINT(booking_id))

    status_err = f'Expected status code - 200, current status code - {part_update.status_code}'
    assert part_update.status_code == 200, status_err
    part_update_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{part_update.json()}'
    assert part_update.json() == exp_booking, part_update_body_err
    get_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{get_booking.json()}'
    assert get_booking.json() == exp_booking, get_body_err


@pytest.mark.partial_update_booking
@pytest.mark.success
def test_partial_update_booking_additionalneeds_param_success(prepare):
    api_client, headers, booking_id = prepare

    additionalneeds = "2 sofas"
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['additionalneeds'] = additionalneeds
    update_data = {'additionalneeds': additionalneeds}
    part_update = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(booking_id), update_data, headers)
    get_booking = api_client.get(GET_BOOKING_ENDPOINT(booking_id))

    status_err = f'Expected status code - 200, current status code - {part_update.status_code}'
    assert part_update.status_code == 200, status_err
    part_update_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{part_update.json()}'
    assert part_update.json() == exp_booking, part_update_body_err
    get_body_err = f'Expected body - \n{exp_booking}, \ncurrent body - \n{get_booking.json()}'
    assert get_booking.json() == exp_booking, get_body_err
