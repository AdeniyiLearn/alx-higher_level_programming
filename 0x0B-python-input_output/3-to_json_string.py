#!/usr/bin/python3
import json

""" This module creates a function to_json_string(my_obj
    returning the JSON representation of an object
    (string))
"""


def to_json_string(my_obj):
    """ Function returns JSON representation
    of an object

    args:
        my_obj : python object

    Returns: strings
    """

    return json.dumps(my_obj)
