def assert_json_object(current_obj, expected_object):
    msg = f'Current object: \n {current_obj} \nExpected object: \n {expected_object}'
    assert current_obj == expected_object, msg