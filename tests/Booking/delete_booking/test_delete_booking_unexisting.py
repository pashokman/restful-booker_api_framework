import pytest

from data.auth.auth_objects import AUTH_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import delete_booking

from utils.assertions.assert_status_code import assert_status_code


@pytest.mark.delete_booking
def test_delete_booking_unexisting():
    token = authorization(AUTH_DATA)

    delete_resp = delete_booking(999999, token)

    assert_status_code(delete_resp.status_code, 405)
    