import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import create_booking_json, get_booking_json, delete_booking

from utils.assertions.assert_schema_validation import assert_schema_validation


schema = {
    'firstname': {'type': 'string', 'minlength': 3, 'required': True},
    'lastname': {'type': 'string', 'minlength': 3, 'required': True},
    'totalprice': {'type': 'number', 'min': 0, 'required': True},
    'depositpaid': {'type': 'boolean', 'required': True},
    'bookingdates': {
        'type': 'dict', 
        'required': True,
        'schema': {
            'checkin': {'type': 'string', 'regex': r'\d{4}-\d{2}-\d{2}', 'required': True},
            'checkout': {'type': 'string', 'regex': r'\d{4}-\d{2}-\d{2}', 'required': True}
        }
    },
    'additionalneeds': {'type': 'string', 'minlength': 0, 'required': False}
}


@pytest.mark.get_booking
@pytest.mark.schema
def test_get_booking_schema():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json.get('bookingid', 'Key not exist')

    get_resp = get_booking_json(booking_id)
    
    assert_schema_validation(get_resp, schema)

    delete_booking(booking_id, token)