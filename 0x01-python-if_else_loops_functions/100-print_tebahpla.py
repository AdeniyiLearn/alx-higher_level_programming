#!/usr/bin/python3
for i, j in zip(range(122, 97, -1), range(89, 63, -1)):
    if i % 2 == 0:
        print('{}{}'.format(chr(i), chr(j)), end='')
