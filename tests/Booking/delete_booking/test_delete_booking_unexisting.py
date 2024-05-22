import pytest

from data.auth.auth_objects import AUTH_DATA
from data.endpoints import AUTH_ENDPOINT, DELETE_BOOKING_ENDPOINT


@pytest.mark.delete_booking
def test_delete_booking_successful(api_client):
    auth = api_client.post(AUTH_ENDPOINT, data=AUTH_DATA)
    token = auth.json()['token']
    headers = {'Cookie': f'token={token}'}

    delete_booking = api_client.delete(DELETE_BOOKING_ENDPOINT(999999), headers=headers)

    del_err_msg = f'Expected status code - 405, current status code - {delete_booking.status_code}'
    assert delete_booking.status_code == 405, del_err_msg
    