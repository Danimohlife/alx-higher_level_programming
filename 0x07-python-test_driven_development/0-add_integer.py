#!/usr/bin/python3
"""
Module for adding two integers.

This module provides a function `add_integer` that takes two arguments and
returns their sum. The function ensures that both arguments are either
integers or floats. If the arguments are floats, they are cast to integers
before performing the addition. If an argument is of an invalid type, a
TypeError is raised.
"""


def add_integer(a, b=98):
    """
    Adds two numbers, ensuring they are integers.

    This function takes two arguments, `a` and `b`, and returns their sum
    after converting any float values to integers. If either `a` or `b` is
    not an integer or float, a TypeError is raised.

    Args:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
        int: The sum of `a` and `b`, after converting any floats to integers.

    Raises:
        TypeError: If `a` or `b` is not an integer or a float.

    Examples:
        >>> add_integer(2, 3)
        5
        >>> add_integer(5.7, 2)
        7
        >>> add_integer(100)
        198
        >>> add_integer("10", 2)
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer
    """

    if b in (None, False):
        b = ""

    if a in (None, False):
        a = ""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
