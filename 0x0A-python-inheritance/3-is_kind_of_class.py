#!/usr/bin/python3
"""
Module to check if an object is an instance of, or
inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Determines if an object is an instance of, or
    inherited from, a specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or
        a subclass of a_class, False otherwise.

    Example:
        >>> is_kind_of_class(42, int)
        True

        >>> is_kind_of_class(42, float)
        False

        >>> is_kind_of_class("Hello", str)
        True

        >>> is_kind_of_class([1, 2, 3], list)
        True

        >>> class Parent:
        ...     pass
        >>> class Child(Parent):
        ...     pass
        >>> is_kind_of_class(Child(), Parent)
        True
    """
    return isinstance(obj, a_class)
