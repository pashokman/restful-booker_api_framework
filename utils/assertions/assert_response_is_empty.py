def assert_response_is_empty(response):
    msg = f'\nActual response: \n{response} \nIS NOT EMPTY.'
    assert response == [], msg