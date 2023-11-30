#!/usr/bin/python3

''' This module creates an empty class called Rectangle'''


class Rectangle:
    '''Defines a rectangle'''
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width.getter(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height.getter(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

