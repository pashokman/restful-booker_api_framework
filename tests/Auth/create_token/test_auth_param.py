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


@pytest.mark.parametrize(
        "login, password", 
        [
            ("", ""), 
            ("non_admin", "password123"), 
            ("admin", "pass123"),
            ("admin", ""),
            ("", "pass123"),
        ]
    )
def test_auth_fail(login, password):
    data = {
            "login": login,
            "password": password
           } 
    response = auth(data)

    assert_status_code(response.status_code, 200)
    assert_obj_in_obj('reason', response.json())
    assert_json_object(response.json()['reason'], 'Bad credentials')
