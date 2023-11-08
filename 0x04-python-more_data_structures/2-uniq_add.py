#!/usr/bin/python3


def uniq_add(my_list=[]):
    """"Adds all unique integers in a list(only once for each int)

    args:
        my_list: list
    """
    if not my_list:
        return []
    score = 0
    element = []
    for idx in my_list:
        num = int(idx)
        element.append(num)
        if element.count(num) > 1:
            continue
        score += num
    return score
