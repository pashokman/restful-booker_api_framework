import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import *

from utils.assertions.assert_schema_validation import assert_schema_list_validation


schema = {
    'bookingid': {'type': 'integer', 'min': 1, 'required': True}
}


@pytest.mark.get_booking_ids
@pytest.mark.schema
def test_get_booking_ids_schema():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json.get('bookingid', 'Key not exist')

    params = {'firstname': 'Lester', 'lastname': 'Tester'}
    get_ids_resp = get_booking_ids_json(params)
    
    assert_schema_list_validation(get_ids_resp, schema)

    delete_booking(booking_id, token)
    