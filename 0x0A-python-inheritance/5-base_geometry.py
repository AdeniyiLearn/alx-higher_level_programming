#!/usr/bin/python3

""" This module creates a class called BaseGeometry"""


class BaseGeometry:
    """An empty class.

        Attributes
        ----------
        NONE

        Methods
        -------

        NONE

        Public Methods
        -------------
        NONE

     """
    pass


if __name__ == "__main__":
    BaseGeometry = __import__('5-base_geometry').BaseGeometry

    bg = BaseGeometry()

    print(bg)
    print(dir(bg))
    print(dir(BaseGeometry))
