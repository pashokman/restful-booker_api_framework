import copy
import pytest

from data.auth.auth_objects import AUTH_DATA
from data.endpoints import AUTH_ENDPOINT, CREATE_BOOKING_ENDPOINT, GET_BOOKING_ENDPOINT, DELETE_BOOKING_ENDPOINT
from data.booking.booking_objects import NEW_BOOKING_DATA


@pytest.mark.create_booking
def test_create_booking_without_additionalneeds(api_client):
    auth = api_client.post(AUTH_ENDPOINT, AUTH_DATA)
    token = auth.json()['token']
    headers = {'Cookie': f'token={token}'}

    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['additionalneeds']
    
    exp_obj = {}
    exp_obj['booking'] = changed_data

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_body = response.json()
    resp_status = response.status_code
    exp_obj['bookingid'] = resp_body['bookingid']
    
    status_err = f'Expected status code - 200. Current status code - {resp_status}'
    assert resp_status == 200, status_err
    body_err = f'Expected body: \n{exp_obj} \nCurrent body: \n{resp_body}'
    assert resp_body == exp_obj, body_err

    get_resp = api_client.get(GET_BOOKING_ENDPOINT(resp_body['bookingid']))
    get_resp_json = get_resp.json()
    get_err_msg = f'Expected object: \n {exp_obj["booking"]} \n Current object: \n {get_resp_json}'
    assert get_resp_json == exp_obj['booking'], get_err_msg

    api_client.delete(DELETE_BOOKING_ENDPOINT(resp_body['bookingid']), headers=headers)