#!/usr/bin/python3

""" This module creates a function called is_same_class(obj, a_class)

function take an obj and check if it is an instance of a class
    and more...
"""


def is_same_class(obj, a_class):
    """ Function checks if an obj is a instance of a class
    and if it is an object of a class that inherits from
    class

    args:
        obj : a python object
        a_class : a python class object

    Returns: True is the obj is an instance of a class and
             False if not
    """
    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    else:
        return False


if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
