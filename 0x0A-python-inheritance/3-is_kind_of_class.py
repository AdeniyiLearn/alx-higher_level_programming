#!/usr/bin/python3

""" This module creates a function called is_kind_of_class(obj, a_class)

function take an obj and check if it is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """ Function checks if an obj is a instance of a class
    and if it is an object of a class that inherits from
    class

    args:
        obj : a python object
        a_class : a python class object

    Returnsi: True is the obj is an instance of a class and 
    False if not
    """
    if isintance(obj, a_class):
        return True
    else:
        return False


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
