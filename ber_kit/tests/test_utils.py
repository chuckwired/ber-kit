from ber_kit.commands import utils

def test_dict_by_key():
    before = [1,2,3]
    key_func = lambda x: x * 2
    after = {2:1, 4:2, 6:3}

    result = utils.dict_by_key(key_func, before)

    assert result == after

def test_dict_by_value():
    before = [1,2,3]
    value_func = lambda x: x + 1
    after = {1:2, 2:3, 3:4}

    result = utils.dict_by_value(value_func, before)

    assert result == after

def test_dict_by_key_and_value():
    before = [1,2,3]
    key_func = lambda x: x * 2
    value_func = lambda x: x + 1
    after = {2:2, 4:3, 6:4}

    result = utils.dict_by_key_and_value(key_func, value_func, before)

    assert result == after
