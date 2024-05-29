import copy
import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import *

from utils.assertions.assert_status_code import assert_status_code
from utils.assertions.assert_json_object import assert_json_object


@pytest.mark.create_booking
@pytest.mark.success
def test_create_booking_success():
    token = authorization(AUTH_DATA)

    create_resp = create_booking(NEW_BOOKING_DATA)
    create_resp_json = create_resp.json()
    
    exp_obj = {}
    exp_obj['booking'] = copy.deepcopy(NEW_BOOKING_DATA)
    exp_obj['bookingid'] = create_resp_json['bookingid']

    assert_status_code(create_resp.status_code, 200)
    assert_json_object(create_resp_json, exp_obj)
    
    get_resp = get_booking_json(create_resp_json['bookingid'])
    assert_json_object(get_resp, exp_obj['booking'])
    
    delete_booking(create_resp_json['bookingid'], token)
