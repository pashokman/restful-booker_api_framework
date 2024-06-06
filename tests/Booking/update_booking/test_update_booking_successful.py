import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA, UPDATE_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import *

from utils.assertions.assert_status_code import assert_status_code
from utils.assertions.assert_json_object import assert_json_object


@pytest.mark.update_booking
@pytest.mark.success
def test_update_booking_successful():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json.get('bookingid', 'Key not exist')

    update_resp = update_booking(booking_id, UPDATE_BOOKING_DATA, token)
    get_resp_json = get_booking_json(booking_id)

    assert_status_code(update_resp.status_code, 200)
    assert_json_object(update_resp.json(), UPDATE_BOOKING_DATA)
    assert_json_object(get_resp_json, UPDATE_BOOKING_DATA)

    delete_booking(booking_id, token)
    