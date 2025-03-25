#!/usr/bin/python3
"""
Module to check if an object is an instance of a subclass of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Determines if an object is an instance of a subclass
    of the specified class.

    This function returns True if `obj` is an instance of a class that
    inherited (directly or indirectly) from `a_class`, but not if it is
    an instance of `a_class` itself.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              but not an instance of a_class itself. False otherwise.

    Example:
        >>> class Parent:
        ...     pass
        >>> class Child(Parent):
        ...     pass
        >>> class GrandChild(Child):
        ...     pass
        >>> inherits_from(Child(), Parent)
        True
        >>> inherits_from(GrandChild(), Parent)
        True
        >>> inherits_from(Parent(), Parent)
        False
        >>> inherits_from(42, int)
        False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
