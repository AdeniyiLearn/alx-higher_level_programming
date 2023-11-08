#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    count = len(my_list)
    index = -1

    if my_list == None:
        return []
    else:
        for num in my_list:
            print("{:d}".format(my_list[index]))
            index -= 1
