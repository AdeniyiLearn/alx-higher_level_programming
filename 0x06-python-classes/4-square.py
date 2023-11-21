#!/usr/bin/python3

"""This module defines class named Square which has an private
    instance attribute called size

size is given int type and value and raises a TypeError if otherwise
"""


class Square:
    """This defines a private instance attribute called size"""
    def __init__(self, size=0):
        """size is defined value.

        args:
            size: integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """to retrieve """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets data"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Public instance method."""
        return self.__size * self.__size
