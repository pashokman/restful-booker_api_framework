import pytest

from utils.methods.booking import get_booking_ids_json

from utils.assertions.assert_response_is_empty import assert_response_is_empty


@pytest.mark.get_booking_ids
def test_get_booking_ids_by_non_existing_firstname():
    params = {'firstname': 'Pdp'}
    get_ids_resp_json = get_booking_ids_json(params)
    
    assert_response_is_empty(get_ids_resp_json)


@pytest.mark.get_booking_ids
def test_get_booking_ids_by_non_existing_lastname():
    params = {'lastname': 'Rorir'}
    get_ids_resp_json = get_booking_ids_json(params)
    
    assert_response_is_empty(get_ids_resp_json)


@pytest.mark.get_booking_ids
def test_get_booking_ids_by_non_existing_checkin():
    params = {'checkin': '3000-08-05'}
    get_ids_resp_json = get_booking_ids_json(params)
    
    # logical error - method should return only bookings with checkin >= '3000-08-05', but it returns also <
    assert_response_is_empty(get_ids_resp_json)


@pytest.mark.get_booking_ids
def test_get_booking_ids_by_non_existing_checkout():
    params = {'checkout': '3000-08-05'}
    get_ids_resp_json = get_booking_ids_json(params)
    
    # logical error - method should return only bookings with checkout >= '2023-11-12', but it returns also <
    assert_response_is_empty(get_ids_resp_json)
