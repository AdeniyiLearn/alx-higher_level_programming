#!/usr/bin/python3
"""This module defines an class variable called __nb_objects, and will be
the base class of all the other classes in this project.

The goal is to manage id attribute in all future classes and to
avoid duplicating the same code (by extension, same bug)"""

import json


class Base:
    """ class defines a public instance attribute called id"""

    __nb_object = 0

    def __init__(self, id=None):
        """ If Id is not None, assign

        args:
            id: public instance integer value
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON rep of list_dictionaries
        Args:
            list_dictionaries: a list of dictionaries
        Returns: JSON string reps
        """
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)
