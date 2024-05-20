import copy
import pytest
from data.auth.auth_objects import AUTH_DATA
from data.endpoints import AUTH_ENDPOINT


@pytest.mark.auth
@pytest.mark.success
def test_auth_correct_credentials(api_client):
    response = api_client.post(AUTH_ENDPOINT, data=AUTH_DATA)

    assert response.status_code == 200
    assert 'token' in response.json()


@pytest.mark.auth
def test_auth_without_credentials(api_client):  
    response = api_client.post(AUTH_ENDPOINT)

    assert response.status_code == 200
    assert 'reason' in response.json()
    assert response.json()['reason'] == 'Bad credentials'


@pytest.mark.auth
def test_auth_incorrect_username(api_client):
    incorrect_data = copy.deepcopy(AUTH_DATA)
    incorrect_data['username'] = 'non_admin'
    
    response = api_client.post(AUTH_ENDPOINT, data=incorrect_data)

    assert response.status_code == 200
    assert 'reason' in response.json()
    assert response.json()['reason'] == 'Bad credentials'


@pytest.mark.auth
def test_auth_incorrect_password(api_client):
    incorrect_data = copy.deepcopy(AUTH_DATA)
    incorrect_data['password'] = 'pass123'
    
    response = api_client.post(AUTH_ENDPOINT, data=incorrect_data)

    assert response.status_code == 200
    assert 'reason' in response.json()
    assert response.json()['reason'] == 'Bad credentials'