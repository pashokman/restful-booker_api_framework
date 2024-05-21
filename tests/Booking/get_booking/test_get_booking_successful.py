import pytest
from data.booking.booking_objects import NEW_BOOKING_DATA
from data.endpoints import GET_BOOKING_ENDPOINT, CREATE_BOOKING_ENDPOINT


@pytest.mark.get_booking
@pytest.mark.success
def test_get_booking_by_all_params_success(api_client):
    response_create = api_client.post(CREATE_BOOKING_ENDPOINT, NEW_BOOKING_DATA)
    bookingid = response_create.json()['bookingid']

    response_get = api_client.get(GET_BOOKING_ENDPOINT(bookingid))
    assert response_get.status_code == 200
    assert response_get.json() == NEW_BOOKING_DATA