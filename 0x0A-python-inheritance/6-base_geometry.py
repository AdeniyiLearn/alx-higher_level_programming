#!/usr/bin/python3

""" This module creates a class called BaseGeometry"""


class BaseGeometry:
    """A class that has only area() public method.
        Public Methods
        -------------
            area(self)
            raise Exception "area() is not implemented"
     """

    def area(self):
        """Raises Exception with below message..."""
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
