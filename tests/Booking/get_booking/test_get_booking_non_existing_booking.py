import pytest
from data.endpoints import GET_BOOKING_ENDPOINT


@pytest.mark.get_booking
def test_get_booking_by_all_params_success(api_client):
    bookingid = 999999

    response_get = api_client.get(GET_BOOKING_ENDPOINT(bookingid))
    assert response_get.status_code == 404