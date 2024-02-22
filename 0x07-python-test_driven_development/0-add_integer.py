#!/usr/bin/python3

"""This Module has only one function called add_integer

add_integer: It comes with a default value in it's second argument
but if a new argument is given it adds the two arguments together.

Prototype
--------
add_integer(a, b=98)

Example
-------

>>>add_integer(4 , 16)
20
>>>add_integer(22)
120
"""


def add_integer(a, b=98):
    '''Function adds 2 integers
    args:
        a: first integer
        b: second integer
    Return: the addition of a and b
    '''
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (a + b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt", verbose=True)
