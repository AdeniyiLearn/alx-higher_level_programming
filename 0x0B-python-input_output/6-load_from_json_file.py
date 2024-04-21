#!/usr/bin/python3

""" This module creates a function load_from_json_file(my_obj, filename)

load_from_json_file(filename) creates an Object from a Json file.
pass
pass
"""
import json


def load_from_json_file(filename):
    """ Function that creates  object from
    a json file

    args:
        filename: python file name
    """

    with open(filename, 'r') as f:
        word = json.load(f)
        return word
