#!/usr/bin/python3


def safe_print_division(a, b):
    """ Divides 2 integers and display result

    args:
        a: first argument
        b: second argument
    Returns: the quotient
    """
    try:
        calc = a / b
    except ZeroDivisionError:
        calc = None
    finally:
        print("Inside result: {}".format(calc))
        return (calc)
