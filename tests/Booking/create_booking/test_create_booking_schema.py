import pytest

from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.booking import *

from utils.assertions.assert_schema_validation import assert_schema_validation


schema = {
    'bookingid': {'type': 'integer', 'required': True},
    'booking': {
        'type': 'dict',
        'required': True,
        'schema': {
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
    }
}


@pytest.mark.create_booking
@pytest.mark.schema
def test_create_booking_schema_validation():
    response = create_booking_json(NEW_BOOKING_DATA)
    assert_schema_validation(response, schema)