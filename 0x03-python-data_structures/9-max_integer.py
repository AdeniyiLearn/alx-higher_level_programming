#!/usr/bin/python3


def max_integer(my_list=[]):
    count = 0
    if len(my_list) == 0:
        return None

    ch1 = my_list[count]

    for i in my_list:
        if(count + 1) < (len(my_list)):
            if ch1 < my_list[count + 1]:
                count = count + 1
                ch1 = my_list[count]
            elif ch1 > my_list[count + 1]:
                count = count + 1
    return ch1
