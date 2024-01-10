#!/usr/bin/python3

def lookup(obj):
    """Function returns a list of attributes and method of an object

    args:
        obj: object as an argument

    Return: attributes and models of a client.

        """
    return obj.__dict__
