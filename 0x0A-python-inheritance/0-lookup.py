#!/usr/bin/python3


def lookup(obj):
    """ Function returns the list of available attributes
    and methods of an object

    args::
        obj : a python object

    Returnsi: a list object
    """

    return help(obj)
