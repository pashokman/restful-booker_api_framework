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


def test_auth_without_credentials():  
    response = auth()

    assert_status_code(response.status_code, 200)
    assert_obj_in_obj('reason', response.json())
    assert_json_object(response.json()['reason'], 'Bad credentials')


def test_auth_incorrect_username():
    incorrect_data = copy.deepcopy(AUTH_DATA)
    incorrect_data['username'] = 'non_admin'
    
    response = auth(incorrect_data)

    assert_status_code(response.status_code, 200)
    assert_obj_in_obj('reason', response.json())
    assert_json_object(response.json()['reason'], 'Bad credentials')


def test_auth_incorrect_password():
    incorrect_data = copy.deepcopy(AUTH_DATA)
    incorrect_data['password'] = 'pass123'
    
    response = auth(incorrect_data)

    assert_status_code(response.status_code, 200)
    assert_obj_in_obj('reason', response.json())
    assert_json_object(response.json()['reason'], 'Bad credentials')


def test_auth_without_username():
    incorrect_data = copy.deepcopy(AUTH_DATA)
    incorrect_data.pop('username', 'Key not exist')
    
    response = auth(incorrect_data)

    assert_status_code(response.status_code, 200)
    assert_obj_in_obj('reason', response.json())
    assert_json_object(response.json()['reason'], 'Bad credentials')


def test_auth_without_password():
    incorrect_data = copy.deepcopy(AUTH_DATA)
    incorrect_data.pop('password', 'Key not exist')
    
    response = auth(incorrect_data)

    assert_status_code(response.status_code, 200)
    assert_obj_in_obj('reason', response.json())
    assert_json_object(response.json()['reason'], 'Bad credentials')
