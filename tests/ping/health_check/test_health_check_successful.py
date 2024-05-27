import pytest

from data.endpoints import HEALTH_CHECK_ENDPOINT


@pytest.mark.health_check
@pytest.mark.success
def test_health_check_successful(api_client):
    health_check = api_client.get(HEALTH_CHECK_ENDPOINT)

    err_msg = f'Expected status code - 201, current status code - {health_check.status_code}'
    assert health_check.status_code == 201, err_msg