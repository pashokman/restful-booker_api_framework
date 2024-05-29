def assert_obj_not_in_obj(inner_obj, outer_obj):
    msg = f'\nInner object: \n{inner_obj} \nIS IN\nOuter object: \n{outer_obj}'
    assert inner_obj not in outer_obj, msg