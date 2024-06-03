import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import *

from utils.assertions.assert_status_code import assert_status_code
from utils.assertions.assert_json_object import assert_json_object


@pytest.mark.get_booking
@pytest.mark.success
def test_get_booking_successful():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json['bookingid']

    get_resp = get_booking(booking_id)
    
    assert_status_code(get_resp.status_code, 200)
    assert_json_object(get_resp.json(), NEW_BOOKING_DATA)

    delete_booking(booking_id, token)
