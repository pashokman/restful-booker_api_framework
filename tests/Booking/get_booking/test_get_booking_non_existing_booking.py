import pytest

from utils.methods.booking import get_booking

from utils.assertions.assert_status_code import assert_status_code


@pytest.mark.get_booking
def test_get_booking_non_existing_id_999999():
    get_resp = get_booking(999999)

    assert_status_code(get_resp.status_code, 404)


@pytest.mark.get_booking
def test_get_booking_non_existing_id_0():
    get_resp = get_booking(0)

    assert_status_code(get_resp.status_code, 404)
