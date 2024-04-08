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
        """Function that divides all elements of a matrix

        parameters:
                matrix: a list of list of integers or floats
                div: none Zero integer or float
        
        Returns: a new matrix
        
        """
        list_copy = []
        max_copy = []
        index = 0

        if not div:
                raise TypeError ("matrix_divided() 1 required argument: 'div'")
        if not isinstance(div, (int, float)):
                raise TypeError ("div must be a number")
        if div == 0:
                raise ZeroDivisionError ("division by zero")

        if isinstance(matrix, list):
                for lst in matrix:
                        if isinstance(lst, list):
                                if index > 0 and len(matrix[index - 1]) != len(matrix[index]):
                                        raise TypeError ("Each row of the matrix must have the same size")
                                for items in lst:
                                        if not isinstance(items, (int, float)):
                                                raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
                                        score = (items/div)
                                        list_copy.append(round(score, 2))
                        else:
                                 raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
                        max_copy.append(list_copy)
                        list_copy = []

                        index += 1
        return (max_copy)



if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
