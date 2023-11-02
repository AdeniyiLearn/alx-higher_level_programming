#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    no_of_args = len(sys.argv) - 1
    score = 0
    for i in range(no_of_args + 1):
        if i != 0:
            score = score + int(sys.argv[i])

    print("{}".format(score))
