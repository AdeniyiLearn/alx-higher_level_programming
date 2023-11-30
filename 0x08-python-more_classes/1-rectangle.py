#!/usr/bin/python3

""" This module creates a class called Rectangle"""


class Rectangle:
    """A class used to create and manage a rectangle.
    
        Attributes
        ----------
        No special class attributes apart from the instantiated ones

        Methods
        -------

        width(self, value)
            manipulates the widths of the rectangle with property decorator

        height(self, value)
            manipulates the rectangle heights
     """

    def __init__(self, width=0, height=0):
        """
        parameters
        ----------

        width : int
            width of each rectangle
        height : int
            height of each rectangle
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Returns the private attribute width """
        return self._width

    @width.setter
    def width(self, value):
        """The method sets the value for width field

        @value: int, raise error if not
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Returns the private attribute height"""
        return self._height

    @height.setter
    def height(self, value):
        """The method sets the value for height field

        @value: int, raise error if not
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

