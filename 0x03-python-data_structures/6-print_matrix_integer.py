#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    count = 0
    for i in matrix:
        if matrix:
            for j in i:
                print('{:d}'.format(j), end='')
        print()
