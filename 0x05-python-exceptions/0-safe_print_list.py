#!/usr/bin/python3
"""
function to print list safely with out
of range index calling
"""


def safe_print_list(my_list=[], x=0):
    """
    safe print list
    function
    """
    value = 0

    while value < x:
        try:
            print("{:}".format(my_list[value]), end="")
            value = value + 1
        except IndexError:
            print()
            return value + 1
    return value + 1
