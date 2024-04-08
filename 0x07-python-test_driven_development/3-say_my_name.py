#!/usr/bin/python3

""" Module contains the function say_my_name

say_my_name : is a function that prints "my name is <first_name> <last_name>"

prototype
---------

say_my_name(first_name, last_name)

Usage:
------

>>> say_my_name("John", "Snow")
"""

def say_my_name(first_name, last_name=""):
        """Function prints My name is <first_name> <last_name>

        parameter:
                first_name: string type
                last_name: string type
        Returns:
                None

        """
        if not isinstance(first_name, str):
                raise TypeError ("first_name must be a string")
        if not isinstance(last_name, str):
                raise TypeError ("last_name must be a string")

        print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/3-say_my_name.txt")

