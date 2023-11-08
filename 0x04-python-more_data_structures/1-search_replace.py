#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """ Replaces all occurences of an element
        by another in a new list.
    args:
        my_list: the initial list.
        search: the element to replace in the list.
        replace: the new element.
    Returns: modified list
    """
    if not my_list:
        return []
    new_list = my_list.copy()
    for num in range(len(new_list)):
        if new_list[num] == search:
            new_list[num] = replace
    return(new_list)
