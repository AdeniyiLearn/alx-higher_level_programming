#!/usr/bin/python3

def lookup(obj):
    """ Function returns the list of available
    attributes and methods of an object

    parameters:
            obj : a python object

    Return:
            a list object
    """
    return(help(obj))
