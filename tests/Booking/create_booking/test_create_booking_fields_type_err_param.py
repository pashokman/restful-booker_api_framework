import copy
import pytest

from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.booking import create_booking

from utils.assertions.assert_status_code import assert_status_code


def set_nested_key(d, key, value):
    keys = key.split(".")
    for k in keys[:-1]:
        d = d.setdefault(k, {})
    d[keys[-1]] = value


@pytest.mark.parametrize("key, value", [
        ("firstname", 123), 
        ("lastname", 123), 
        ("totalprice", "price"), 
        ("totalprice", 123.45), 
        ("depositpaid", "deposit"), 
        ("bookingdates", "some_str"), 
        ("bookingdates.checkin", 321), 
        ("bookingdates.checkout", 321), 
        ("additionalneeds", 321), 
    ]
)
@pytest.mark.create_booking
def test_create_booking_firstname_not_string(key, value):
    booking_copy = copy.deepcopy(NEW_BOOKING_DATA)
    set_nested_key(booking_copy, key, value)

    response = create_booking(booking_copy)
    assert_status_code(response.status_code, 500)
