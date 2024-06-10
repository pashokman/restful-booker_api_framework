import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA, UPDATE_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import create_booking_json, delete_booking, partial_update_boking_json

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


@pytest.mark.partial_update_booking
@pytest.mark.schema
def test_partial_update_booking_all_params_schema():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json.get('bookingid', 'Key not exist')

    part_upd_resp = partial_update_boking_json(booking_id, UPDATE_BOOKING_DATA, token)

    assert_schema_validation(part_upd_resp, schema)

    delete_booking(booking_id, token)