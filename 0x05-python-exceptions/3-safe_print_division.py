#!/usr/bin/python3
"""
print save divison
"""


def safe_print_division(a, b):
    """
    save division
    """

    try:
        print("Inside result: {:}".format(a / b))
    except (ZeroDivisionError, TypeError, ValueError):
        print("Inside result: {:s}".format("None"))
    finally:
        if b:
            return a / b
        return None
