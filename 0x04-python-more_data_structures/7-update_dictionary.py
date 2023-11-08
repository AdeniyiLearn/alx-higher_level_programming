#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """"Replaces or adds key/value in a dictionary

    args:
        a_dictionary: dictionary argument.
        key: a new key.
        value: a new value for the key.

    Returns: Nothing
    """
    if isinstance(key, str):
        a_dictionary[key] = value

    return (a_dictionary)
