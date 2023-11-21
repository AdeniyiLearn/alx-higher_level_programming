#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Prints only integers in the first x elements in a list

    args:
        my_list: list contain varying types
        x(int): total elements index to be covered
    Returns: Total number of element eventually printed
    """
    count = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            count = count + 1
        except(TypeError, ValueError):
            continue

    print()
    return (count)
