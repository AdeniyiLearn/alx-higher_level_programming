#!/usr/bin/python3

"""This module defines class named Square which has an private
    instance attribute called size

size doesn't have any type or value for now
"""


class Square:
    """This defines a private instance attribute called size"""
    def __init__(self, size):
        """size is defined typeless and without value """
        self.__size = size
