#!/usr/bin/python3
for r in range(97, 123):
    if chr(r) == 'q' or chr(r) == 'e':
        continue
    print("{}".format(chr(r)), end='')
