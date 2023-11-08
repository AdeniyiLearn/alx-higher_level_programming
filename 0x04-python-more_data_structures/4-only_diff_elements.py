#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """"Returns a set of elements present in only one set

    args:
        set_1: first set
        set_2: second set

    Returns: new set with common item from the 2 previous sets
    """
    return set_1 ^ set_2
