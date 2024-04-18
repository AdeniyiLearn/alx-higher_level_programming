#!/usr/bin/python3

""" This module creates a function called inherits_from(obj, a_class)

function take an obj and check if it is an instance of a class"""


def inherits_from(obj, a_class):
    """ Function checks if an obj is a instance of a class
    and if it is directly or indirectly from the class
    class

    args:
        obj : a python object
        a_class : a python class object

    Returns: True is the obj is an instance of a class and
    False if not
    """
    if issubclass(type(obj), a_class) and a_class != type(obj):
        return True
    else:
        return False


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
