from cerberus import Validator


def assert_schema_validation(current_object, schema):
    validator = Validator(schema)
    assert validator.validate(current_object), validator.errors


def assert_schema_list_validation(current_object, schema):
    validator = Validator(schema)

    if not current_object:
        assert False, "Validation failed: Response is empty."
    else:
        all_valid = True
        for item in current_object:
            if not validator.validate(item):
                all_valid = False
                assert all_valid, f"Validation errors in item {item}: {validator.errors}"
        assert all_valid