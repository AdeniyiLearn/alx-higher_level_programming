#!/usr/bin/python3


def best_score(a_dictionary):
    """"Return a key with the biggest integer value.

    args:
        a_dictionary: dictionary argument.

    Returns: a key with biggest value
    """
    compare = 0
    holder = ''
    if a_dictionary and isinstance(a_dictionary, dict):
        for key, pair in a_dictionary.items():
            if compare <= pair:
                compare = pair
                holder = key

        return holder
