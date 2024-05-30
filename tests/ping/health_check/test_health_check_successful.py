import pytest

from utils.methods.health_check import health_check

from utils.assertions.assert_status_code import assert_status_code


@pytest.mark.health_check
@pytest.mark.success
def test_health_check_successful():
    hc = health_check()
    assert_status_code(hc.status_code, 201)