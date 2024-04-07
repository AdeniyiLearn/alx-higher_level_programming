#!/usr/bin/python3

"""Module contain the function matrix_divide
matrix_divide : is a function that divides all the elements
in a matrix by a given number --div--.

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
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    row_size = len(matrix[0])
    new_matrix = []
    for list in matrix:
        if len(list) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        newlist = []
        for item in list:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            newlist.append(int(item/div))
        new_matrix.append(newlist)
    
    return(new_matrix)




if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
