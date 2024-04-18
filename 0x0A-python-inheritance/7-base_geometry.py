#!/usr/bin/python3

""" This module creates a class called BaseGeometry"""


class BaseGeometry:
    """A class that has only two public method.
        Public Methods
        -------------
            area(self)
            raise Exception "area() is not implemented"

            integer_validator(self, name, value):
            it validates value
     """
    def area(self):
        """Returns the area of rectangle"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """it validates value

        args:
            name: a string
            value: a integer
        """
        if not isinstance(value, int):
            raise TypeError ("<name> must be an integer")
        if value <= 0:
            raise ValueError ("<name> must be greater than 0")



if __name__ == "__main__":
    BaseGeometry = __import__('7-base_geometry').BaseGeometry

    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
