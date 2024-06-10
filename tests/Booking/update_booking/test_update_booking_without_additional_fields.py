import copy
import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA, UPDATE_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import create_booking_json, delete_booking, update_booking, get_booking_json

from utils.assertions.assert_status_code import assert_status_code
from utils.assertions.assert_json_object import assert_json_object


@pytest.fixture
def preparation():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json['bookingid']

    changed_data = copy.deepcopy(UPDATE_BOOKING_DATA)

    yield token, booking_id, changed_data

    delete_booking(booking_id, token)


@pytest.mark.update_booking
@pytest.mark.success
def test_update_booking_without_additionalneeds(preparation):
    token, booking_id, changed_data = preparation
    changed_data.pop('additionalneeds', 'Key not exist')

    exp_obj = UPDATE_BOOKING_DATA
    exp_obj['additionalneeds'] = NEW_BOOKING_DATA['additionalneeds']
    
    update_resp = update_booking(booking_id, changed_data, token)
    get_resp_json = get_booking_json(booking_id)

    assert_status_code(update_resp.status_code, 200)
    assert_json_object(update_resp.json(), exp_obj)
    assert_json_object(get_resp_json, exp_obj)
    