#!/usr/bin/python3

"""This module defines a function named lookup, it returns the
list of the attributes and methods of an object
"""


def lookup(obj):
    """Function returns a list of attributes and method of an object

    args:
        obj: object as an argument

    Return: attributes and models of a client.

        """
    return obj.__dict__
