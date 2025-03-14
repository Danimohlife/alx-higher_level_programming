#!/usr/bin/python3

"""
print interger saferly
"""


def safe_print_integer(value):
    """
    function to print int value safe
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False

    return True
