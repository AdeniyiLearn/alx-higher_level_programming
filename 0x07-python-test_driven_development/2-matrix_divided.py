#!/usr/bin/python3

"""Module contain the function matrix_divide
matrix_divide : is a function that divides all the elements
in a matrix.

Prototype
---------

    matrix_divide(matrix, div)

Usage Example:
--------------
    >>>matrix = [[3, 4, 6], [23, 24, 26]]
    >>>matrix_divided(matrix, 2)
"""

def matrix_divided(matrix, div):
"""function divides all elements of a matrix
args:
    matrix: a list of lists
    div: integer divisor
Return: a new matrix
"""



if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
