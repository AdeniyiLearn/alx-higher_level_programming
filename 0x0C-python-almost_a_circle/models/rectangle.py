#!/usr/bin/python3
"""This module defines a class Rectangle which inherits from another
class called BAse.

it uses settera and getters to protect attributes like:
width and height"""

from base import Base


class Rectangle(Base):
    """A class that inherits from class Base, used to create and
    manage a rectangle.

        Attributes
        ----------
            width: rectangle wideness
            height: rectangle height
            x: integer value
            y: integer value
            id: public instance integer value from Base

        Methods
        -------
        None
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """

        args:
            width: rectangle wideness
            height: rectangle height
            x: integer value
            y: integer value
            id: public instance integer value from Base
        """
        super().__init__(id=None)

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """Returns the private attribute width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """The method sets the value for width field

        args:
            value: int, raise error if not
        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the private attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """The method sets the value for height field for Rectangle

        args:
            value: int, raise error if not
        Returns: None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
