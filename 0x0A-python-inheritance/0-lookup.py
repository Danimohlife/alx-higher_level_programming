#!/usr/bin/python3
"""
Module: lookup

This module defines a function `lookup` that returns the list of
available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: A list of strings representing the
        object's attributes and methods.

    Example:
        >>> class MyClass:
        ...     def method(self):
        ...         pass
        >>> obj = MyClass()
        >>> lookup(obj)
        ['__class__', '__delattr__', '__dict__', '__dir__', ..., 'method']
    """
    return dir(obj)
