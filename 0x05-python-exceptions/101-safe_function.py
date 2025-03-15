#!/usr/bin/python3
"""
safe function calls
"""
import sys


def safe_function(fct, *args):
    """
    call function safely
    """

    try:
        return fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
