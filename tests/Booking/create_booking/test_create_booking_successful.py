import copy
import pytest

from data.auth.auth_objects import AUTH_DATA
from data.endpoints import AUTH_ENDPOINT, CREATE_BOOKING_ENDPOINT, GET_BOOKING_ENDPOINT, DELETE_BOOKING_ENDPOINT
from data.booking.booking_objects import NEW_BOOKING_DATA


@pytest.mark.create_booking
@pytest.mark.success
def test_create_booking_success(api_client):
    auth = api_client.post(AUTH_ENDPOINT, AUTH_DATA)
    token = auth.json()['token']
    headers = {'Cookie': f'token={token}'}

    exp_obj = {}
    exp_obj['booking'] = copy.deepcopy(NEW_BOOKING_DATA)

    create_resp = api_client.post(CREATE_BOOKING_ENDPOINT, NEW_BOOKING_DATA)
    resp_json = create_resp.json()
    exp_obj['bookingid'] = resp_json['bookingid']

    create_err_msg = f'Expected object: \n {exp_obj} \n Current object: \n {resp_json}'
    assert resp_json == exp_obj, create_err_msg
    
    get_resp = api_client.get(GET_BOOKING_ENDPOINT(resp_json['bookingid']))
    get_resp_json = get_resp.json()
    get_err_msg = f'Expected object: \n {exp_obj["booking"]} \n Current object: \n {get_resp_json}'
    assert get_resp_json == exp_obj['booking'], get_err_msg
    
    api_client.delete(DELETE_BOOKING_ENDPOINT(resp_json['bookingid']), headers=headers)