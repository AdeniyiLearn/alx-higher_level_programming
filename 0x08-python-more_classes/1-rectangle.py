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
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

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



if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)
    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
