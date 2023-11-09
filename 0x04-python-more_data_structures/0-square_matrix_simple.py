#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    '''computes the square value of all matrix integer.

    args:
        matrix: a list of 3 lists(2 dimensional array.
    Returns: new list modified as squares of previous data).
    '''
    new_matrix = [[element**2 for element in block] for block in matrix]
    return(new_matrix)
