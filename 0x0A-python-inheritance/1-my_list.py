#!/usr/bin/python3

""" This module creates a class called Rectangle"""


class Mylist(list):
    """A class that inherits from list

        Attributes
        ----------
        No special class attributes apart from the instantiated ones

        Methods
        -------

        print_sorted(self):
            prints the list, but sorted and ascending sort.

     """


    def __init__(self, *args):
                """
        parameters
        ----------

        args : 
            multiple arguments
        kwargs : 
            multiple arguments
        """
        super().__init__(*args, **kwargs)
        self.args = args;


    def print_sorted(self):
        '''prints the list, but sorted(ascending)'''
        print(self)

    def __str__(self):
        '''Returns # values for rectangle representation'''

    def __repr__(self):
        """"returns strings represention of the intance"""
        return f"Rectangle({self.__width}, {self.__height})"
