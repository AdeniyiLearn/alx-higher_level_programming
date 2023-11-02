#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    no_of_args = len(sys.argv) - 1
    if no_of_args == 0:
        print('0 arguments.')
    elif no_of_args == 1:
        print('{} argument:'.format(no_of_args))
    else:
        print("{} arguments:".format(no_of_args))

    for i in range(no_of_args + 1):
        if i != 0:
            print("{}: {}".format(i, sys.argv[i]))
