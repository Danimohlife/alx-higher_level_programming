#!/usr/bin/python3
import sys
"""
save print int with text xpect
"""


def safe_print_integer_err(value):
    """
    std int text
    """

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
