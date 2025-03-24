#!/usr/bin/python3
"""
LockedClass module
This module defines a class that prevents dynamic attribute creation,
except for an attribute named `first_name`.
"""


class LockedClass:
    """
    A class that prevents the user from dynamically
    creating new instance attributes,
    except if the attribute is called `first_name`.
    """

    __slots__ = ["first_name"]

    def __init__(self, first_name=None):
        """
        Initializes a LockedClass instance.

        Args:
            first_name (str, optional): The first
            name to be set. Defaults to None.
        """
        if first_name is not None:
            self.first_name = first_name
