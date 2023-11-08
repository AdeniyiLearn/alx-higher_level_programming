#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return []
    else:
        count = len(my_list)
        index = -1
        for num in my_list:
            print("{:d}".format(my_list[index]))
            index -= 1
