import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import create_booking_json, get_booking, delete_booking

from utils.assertions.assert_status_code import assert_status_code


@pytest.mark.delete_booking
@pytest.mark.success
def test_delete_booking_successful():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json.get('bookingid', 'Key not exist')

    delete_resp = delete_booking(booking_id, token)
    get_resp = get_booking(booking_id)

    assert_status_code(delete_resp.status_code, 201)
    assert_status_code(get_resp.status_code, 404)
    