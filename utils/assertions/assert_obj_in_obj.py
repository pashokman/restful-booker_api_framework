def assert_obj_in_obj(inner_obj, outer_obj):
    msg = f'\nInner object: \n{inner_obj} \nIS NOT IN \nOuter object: \n{outer_obj}'
    assert inner_obj in outer_obj, msg