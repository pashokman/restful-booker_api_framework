import pytest

from data.auth.auth_objects import AUTH_DATA

from utils.methods.authorization import auth

from utils.assertions.assert_schema_validation import assert_schema_validation


schema = {
    'token': {'type': 'string', 'required': True}
}


@pytest.mark.auth
@pytest.mark.schema
def test_auth_schema():
    response = auth(AUTH_DATA)
    assert_schema_validation(response.json(), schema)
