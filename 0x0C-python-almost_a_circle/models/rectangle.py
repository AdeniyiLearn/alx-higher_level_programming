#!/usr/bin/python3

"""This module defines a class Rectangle which inherits from another
class called BAse
"""

from models.base import Base


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
            public methods
            --------------
            area(self)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes each Rectangle object

        args:
            width: rectangle wideness
            height: rectangle height
            x: integer value
            y: integer value
            id: public instance integer value from Base
        """

        super().__init__(id)

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
        """Returns the private attribute width"""
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
        if value <= 0:
            raise ValueError("width must be > 0")
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
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns the private attribute x"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """The method sets the value for x cordinates for Rectangle

        args:
            x : integer value not less than zero
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Returns private attribute y"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """Method sets the value for y cordinates

        args:
            x : integer value
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """prints # representation of Rectangle instances"""
        for f in range(self.__y):
            print()
        for i in range(self.__height):
            for g in range(self.__x):
                print(" ", end='')
            for u in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args):
        """Method assigms an argument to each attribut

        args:
            *args: multiple non keyword arguments
        """
        if args and len(args) != 0:
            for arg in args:
                if len(args) == 1:
                    self.id = args[0]
                elif len(args) == 2:
                    self.id = args[0]
                    self.__width = args[1]
                elif len(args) == 3:
                    self.id = args[0]
                    self.__width = args[1]
                    self.__height = args[2]
                elif len(args) == 4:
                    self.id = args[0]
                    self.__width = args[1]
                    self.__height = args[2]
                    self.__x = args[3]
                else:
                    self.id = args[0]
                    self.__width = args[1]
                    self.__height = args[2]
                    self.__x = args[3]

    def __str__(self):
        """Returns informal info representation of object"""
        return ("[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id, self.__x,
            self.__y, self.__width, self.__height))
