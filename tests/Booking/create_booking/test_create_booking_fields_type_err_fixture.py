import copy
import pytest

from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.booking import create_booking

from utils.assertions.assert_status_code import assert_status_code


@pytest.fixture(params=[
        ("firstname", 123), 
        ("lastname", 123), 
        ("totalprice", "price"), 
        ("totalprice", 123.45), 
        ("depositpaid", "deposit"), 
        ("bookingdates", "some_str"), 
        ("bookingdates.checkin", 321), 
        ("bookingdates.checkout", 321), 
        ("additionalneeds", 321), 
    ],
    ids=lambda param: f"{param[0]}-{param[1]}"
)
def input_data(request):
    return request.param


def set_nested_key(d, key, value):
    keys = key.split(".")
    for k in keys[:-1]:
        d = d.setdefault(k, {})
    d[keys[-1]] = value


@pytest.mark.create_booking
def test_create_booking_firstname_not_string(input_data):
    key, value = input_data
    booking_copy = copy.deepcopy(NEW_BOOKING_DATA)
    set_nested_key(booking_copy, key, value)

    response = create_booking(booking_copy)
    assert_status_code(response.status_code, 500)
