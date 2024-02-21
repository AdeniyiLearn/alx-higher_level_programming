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

        Public Methods
        -------------
        area(self)
            returns the area of rectangle i.e  width * height

        perimeter(self)
            returns the perimeter of a rectangle i.e 2(width + height
            or 0 if any of h or w is 0

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

    def __del__(self):
        print("Bye rectangle...")

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

    def area(self):
        '''Returns the area of rectangle '''
        return (self.__height * self.__width)

    def perimeter(self):
        '''Returns the perimeter of rectangle and 0 if h or w are 0'''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        '''Returns # values for rectangle representation'''
        result = ''
        for i in range(self.__height):
            for u in range(self.__width):
                result += '#'
            if i < (self.__height - 1):
                result += '\n'
        return (result)

    def __repr__(self):
        """"returns strings represention of the intance"""
        return f"Rectangle({self.__width}, {self.__height})"


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)
    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
