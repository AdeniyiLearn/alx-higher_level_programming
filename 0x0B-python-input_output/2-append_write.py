#!/usr/bin/python3

""" This module creates a function append_write() that
    appends a string and returns the number of
    character added
"""


def append_write(filename="", text=""):
    """ Function appends a string at the end of
    a text file.

    args:
        filename : file object
        text : string object

    Returns: the number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)


if __name__ == "__main__":
    append_write = __import__('2-append_write').append_write

    nb_characters_added = append_write("file_append.txt", "This School \
        is so cool!\n")
    print(nb_characters_added)
