#!/usr/bin/python3

""" This module creates a function save_to_json_file(my_obj, filename)

save_to_json_file(my_obj, filename) writes an Object to text file.
using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function writes object to a
    textfile using JSON rep

    args:
        my_obj : python object
        filename: python file name
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
