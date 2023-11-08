#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    list_1 = []
    list_2 = []
    dull = 0
    if len(tuple_a) >= 2:
        for i in range(2):
            list_1.append(tuple_a[i])
    elif len(tuple_a) == 1:
        list_1.append(tuple_a)
        list_1.append(dull)
    else:
        list_1.append(dull)
        list_1.append(dull)

    if len(tuple_b) >= 2:
        for i in range(2):
            list_2.append(tuple_b[i])
    elif len(tuple_b) == 1:
        list_2.append(tuple_b[0])
        list_2.append(dull)
    else:
        list_2.append(dull)
        list_2.append(dull)

    tuple_c = list(zip(list_1, list_2))
    a = sum(tuple_c[0])
    b = sum(tuple_c[1])
    return a, b
