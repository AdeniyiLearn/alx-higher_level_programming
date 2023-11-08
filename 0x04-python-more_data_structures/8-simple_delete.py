#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """"deletes a key in a dictionary.

    args:
        a_dictionary: dictionary argument.
        key: the key to be deleted.

    Returns: Nothing
    """
    if key in a_dictionary and isinstance(key, str):
        del a_dictionary[key]

    return (a_dictionary)
