#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """"Return a new dictionary with all values multiplied by 2

    args:
        a_dictionary: dictionary argument.

    Returns: a new dictionary
    """
    new_dic = {}
    for key, pair in a_dictionary.items():
        new_dic[key] = pair * 2

    return new_dic
