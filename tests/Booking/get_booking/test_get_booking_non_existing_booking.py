import pytest
from data.endpoints import GET_BOOKING_ENDPOINT


@pytest.mark.get_booking
def test_get_booking_non_existing_id_999999(api_client):
    response_get = api_client.get(GET_BOOKING_ENDPOINT(999999))
    assert response_get.status_code == 404


@pytest.mark.get_booking
def test_get_booking_non_existing_id_0(api_client):
    response_get = api_client.get(GET_BOOKING_ENDPOINT(0))
    assert response_get.status_code == 404