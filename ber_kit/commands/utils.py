
def dict_by_key(key_function, values):
    """
    Convert a list into a dictionary, using a function
    to create your key and the list item as the value.
    """
    return dict((key_function(v), v) for v in values)

def dict_by_value(value_function, keys):
    """
    Convert a list into a dictionary, using a function
    to create your values and the list item as the key.
    """
    return dict((k, value_function(k)) for k in keys)

def dict_by_key_and_value(key_function, value_function, items):
    """
    Convert items into a dict, transforming it with a key
    function and a value function.
    """
    return dict((key_function(i), value_function(i)) for i in items)
