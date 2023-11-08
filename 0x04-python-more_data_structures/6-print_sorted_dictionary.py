#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """"Prints a dictionary by ordered keys

    args:
        a_dictionary: dictionary argument.

    Returns: Nothing
    """
    for key, pair in sorted(a_dictionary.items()):
        print("{}: {}".format(key, pair))
