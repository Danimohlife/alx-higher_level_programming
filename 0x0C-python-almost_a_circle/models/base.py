#!/usr/bin/python3
"""
This module defines the Base class.

The Base class serves as a foundation for managing unique object IDs.
"""


class Base:
    """
    Base class to manage unique IDs for derived objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int, optional): If provided, assigns it to the instance.
            Otherwise, increments __nb_objects and assigns the new value.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
