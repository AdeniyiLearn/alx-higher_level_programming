#!/usr/bin/python3

""" This module creates a function read_file(filename="")
    that reads a text file (UTF-8) and prints to stdout:
"""


def read_file(filename=""):
    """ Function read a text file and prints
    to stdout

    args:
        filename : a python object

    Returns: None
    """

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')


if __name__ == "__main__":
    read_file = __import__('0-read_file').read_file

    read_file("my_file_0.txt")
