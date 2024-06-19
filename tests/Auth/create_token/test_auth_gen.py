import copy
import pytest

from data.auth.auth_objects import AUTH_DATA

from utils.methods.authorization import auth

from utils.assertions.assert_json_object import assert_json_object
from utils.assertions.assert_obj_in_obj import assert_obj_in_obj
from utils.assertions.assert_status_code import assert_status_code


pytestmark = pytest.mark.auth


@pytest.mark.success
def test_auth_correct_credentials():
    response = auth(AUTH_DATA)

    assert_status_code(response.status_code, 200)
    assert_obj_in_obj('token', response.json())


def pytest_generate_tests(metafunc):
    if "login_data" in metafunc.fixturenames:
        metafunc.parametrize("login_data", [
            ("", ""), 
            ("non_admin", "password123"), 
            ("admin", "pass123"),
            ("admin", ""),
            ("", "pass123"),
        ],
        ids=lambda param: f"{param[0]}-{param[1]}"
        )


def test_auth_fail(login_data):
    login, password = login_data
    data = {
            "login": login,
            "password": password
           }
    response = auth(data)

    assert_status_code(response.status_code, 200)
    assert_obj_in_obj('reason', response.json())
    assert_json_object(response.json()['reason'], 'Bad credentials')
