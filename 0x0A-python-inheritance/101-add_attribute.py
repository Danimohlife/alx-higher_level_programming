#!/usr/bin/python3
"""
setattr for an object
"""


def add_attribute(obj, var, val):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to modify.
        var (str): The name of the attribute to add.
        val: The value to set for the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, var, val)
