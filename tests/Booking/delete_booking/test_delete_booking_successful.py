import pytest
from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA
from data.endpoints import AUTH_ENDPOINT, CREATE_BOOKING_ENDPOINT, GET_BOOKING_ENDPOINT, DELETE_BOOKING_ENDPOINT


@pytest.mark.delete_booking
@pytest.mark.success
def test_delete_booking_successful(api_client):
    auth = api_client.post(AUTH_ENDPOINT, data=AUTH_DATA)
    token = auth.json()['token']

    create_booking = api_client.post(CREATE_BOOKING_ENDPOINT, NEW_BOOKING_DATA)
    booking_id = create_booking.json()['bookingid']

    headers = {'Cookie': f'token={token}'}
    delete_booking = api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id), headers=headers)
    get_booking = api_client.get(GET_BOOKING_ENDPOINT(booking_id))

    del_err_msg = f'Expected status code - 201, current status code - {delete_booking.status_code}'
    assert delete_booking.status_code == 201, del_err_msg
    get_err_msg = f'Expected status code - 404, current status code - {get_booking.status_code}'
    assert get_booking.status_code == 404, get_err_msg