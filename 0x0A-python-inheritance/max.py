#!/usr/bin/python3

""" This module creates a function called lookup"""


def lookup(obj):
    """ Function returns the list of available attributes
    and methods of an object

    args::
        obj : a python object

    Returnsi: a list object
    """

    return dir(obj)
