#!/usr/bin/python3

""" This module creates a class called BaseGeometry"""


class BaseGeometry:
    """A class that has only area() public method.

        Attributes
        ----------
        NONE

        Methods
        -------

        NONE

        Public Methods
        -------------
            area(self)
            raise Exception "area() is not implemented"

     """

    def area(self):
        '''Returns the area of rectangle '''
        raise Exception ("area() is not implemented")


if __name__ == "__main__":
    BaseGeometry = __import__('6-base_geometry').BaseGeometry

    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
