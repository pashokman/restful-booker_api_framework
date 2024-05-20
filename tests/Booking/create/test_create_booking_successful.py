import pytest
import copy
from data.endpoints import CREATE_BOOKING_ENDPOINT
from data.booking.booking_objects import NEW_BOOKING_DATA


@pytest.mark.create_booking
@pytest.mark.success
def test_create_booking_success(api_client):
    exp_obj = {}
    exp_obj['booking'] = copy.deepcopy(NEW_BOOKING_DATA)

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=NEW_BOOKING_DATA)
    resp_json = response.json()
    exp_obj['bookingid'] = resp_json['bookingid']

    err_msg = f'Expected object: \n {exp_obj} \n Current object: \n {resp_json}'
    assert resp_json == exp_obj, err_msg