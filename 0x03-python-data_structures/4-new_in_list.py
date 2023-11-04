#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    use_list = my_list[:]
    if idx < 0 or idx >= len(use_list):
        return my_list
    else:
        use_list[idx] = element
        return use_list
