#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """ Divides element by element 2 lists

    args:
        my_list_1(contains any type): first list
        my_list_2(contains any type): second list argument
        list_length: can be bigger than length of both list
    Returns: a new list (length = list) with all divisions
    """
    score = 0
    new_list = []
    for idx in range(list_length):
        try:
            score = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            score = 0
            print("division by 0")
        except (TypeError, ValueError):
            score = 0
            print("wrong type")
        except IndexError:
            score = 0
            print("out of range")
        finally:
            new_list.append(score)
    return (new_list)
