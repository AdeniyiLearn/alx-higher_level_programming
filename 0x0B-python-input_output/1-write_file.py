#!/usr/bin/python3

""" This module creates a function write_file(filename="", text="")
    that writes a string to a text file (UTF8) and returns the number
    of characters written:
"""


def write_file(filename="", text=""):
    """ Function writes a string to a text file.

    args:
        filename : file object
        text : string object

    Returns: the number of characters written
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)


if __name__ == "__main__":
    write_file = __import__('1-write_file').write_file

    nb_characters = write_file("my_first_file.txt", "This School \
            is so cool!\n")
    print(nb_characters)
