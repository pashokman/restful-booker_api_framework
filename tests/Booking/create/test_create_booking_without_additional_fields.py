import pytest
import copy
from data.endpoints import CREATE_BOOKING_ENDPOINT
from data.booking.booking_objects import NEW_BOOKING_DATA


@pytest.mark.create_booking
def test_create_booking_without_additionalneeds(api_client):
    changed_data = copy.deepcopy(NEW_BOOKING_DATA)
    del changed_data['additionalneeds']
    
    exp_obj = {}
    exp_obj['booking'] = changed_data

    response = api_client.post(CREATE_BOOKING_ENDPOINT, data=changed_data)
    resp_body = response.json()
    resp_status = response.status_code
    exp_obj['bookingid'] = resp_body['bookingid']
    
    exp_status = 200
    err_status = f'Expected status code - {exp_status}. Current status code - {resp_status}'
    assert resp_status == exp_status, err_status
    err_body = f'Expected body: \n{exp_obj} \nCurrent body: \n{resp_body}'
    assert resp_body == exp_obj, err_body