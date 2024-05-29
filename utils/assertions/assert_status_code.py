def assert_status_code(current_status, expected_status):
    msg = f'\nCurrent status code: - {current_status} \nExpected status code: - {expected_status}'
    assert current_status == expected_status, msg