#!/usr/bin/python3

""" Module contains the function print_square

print_square : is a function that prints a square with the character #

prototype
---------

print_square(2)

Usage:
------

>>> print_square(4)
"""

def print_square(size):
    """Function that print a square with the character #
        
        parameter:
                size: length of the square
        Returns:
                None
    """
    if isinstance(size, float) and size < 0:
          raise TypeError ("size must be an integer")
    if not isinstance(size, int):
        raise TypeError ("size must be an integer")
    if size < 0:
        raise ValueError ("size must be >= 0")
        for i in range(size):
                for u in range(size):
                        print("#", end = '')
                print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/4-print_square.txt")

