#!/usr/bin/python3


def safe_print_integer(value):
    """ Prints all list's element that's integer

    args:
        value: integer value to be printed
    Returns: True is value is int or False if it is not
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return False
    else:
        return True
