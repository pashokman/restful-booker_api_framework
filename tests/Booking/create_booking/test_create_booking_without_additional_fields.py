import copy
import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import *

from utils.assertions.assert_status_code import assert_status_code
from utils.assertions.assert_json_object import assert_json_object


@pytest.mark.create_booking
def test_create_booking_without_additionalneeds(api_client):
    token = authorization(api_client, AUTH_DATA)

    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['additionalneeds']
    
    create_resp = create_booking(api_client, changed_data)
    create_resp_json = create_resp.json()

    exp_obj = {}
    exp_obj['booking'] = changed_data
    exp_obj['bookingid'] = create_resp_json['bookingid']

    assert_status_code(create_resp.status_code, 200)
    assert_json_object(create_resp_json, exp_obj)

    get_resp = get_booking_json(api_client, create_resp_json['bookingid'])
    assert_json_object(get_resp, exp_obj['booking'])

    delete_booking(api_client, create_resp_json['bookingid'], token)