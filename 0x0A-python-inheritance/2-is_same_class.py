#!/usr/bin/python3
"""
Module to check if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Determines if an object is exactly an instance of the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.

    Example:
        >>> is_same_class(42, int)
        True

        >>> is_same_class(42, float)
        False

        >>> is_same_class("Hello", str)
        True

        >>> is_same_class([1, 2, 3], list)
        True

        >>> class Parent:
        ...     pass
        >>> class Child(Parent):
        ...     pass
        >>> is_same_class(Child(), Parent)
        False

    """
    return type(obj) is a_class
