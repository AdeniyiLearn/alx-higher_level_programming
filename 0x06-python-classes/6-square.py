#!/usr/bin/python3

"""This module defines class named Square which has an private
    instance attribute called size

size is given int type and value and raises a TypeError if otherwise
"""


class Square:
    """This defines a private instance attribute called size"""
    def __init__(self, size=0, position=(0, 0)):
        """size is defined value.

        args:
            size: integer.
            position: tuple of 2 positive integers.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        for val in range(len(position)):
            if position[val] < 0 or val > 1:
                raise TypeError("position must be a tuple \
                        2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """retrieve position """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ mutate the position.

        args:
            value: 2 positive integr tuple.
        """
        for val in range(len(position)):
            if position[val] < 0 or val > 1:
                raise TypeError("position must be a tuple\
                        of 2 positive integers")
        self.__position = value

    def area(self):
        """ Public instance method."""
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character # """
        if self.__size == 0:
            print()
            return
        else:
            for hor in range(self.__size):
                if not self.__position[1] > 0:
                    for line in range(self.__position[0]):
                        print("-", end="")
                for val in range(self.__size):
                    print("#", end="")
                print()
