#!/usr/bin/python3
"""
raise name exception with a text
"""


def raise_exception_msg(message=""):
    """
    name error exception to be raised
    """
    try:
        raise NameError(message)
    except NameError as me:
        raise me
