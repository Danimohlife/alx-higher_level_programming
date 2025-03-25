#!/usr/bin/python3
"""
Module defining a base class for geometric shapes.
"""


class BaseGeometry:
    """
    A base class for geometric operations.

    This class serves as a blueprint for geometric shapes. It defines a method
    `area`, which must be implemented by subclasses.

    Methods:
        area(self): Raises an Exception, indicating it must be implemented
        by subclasses.

    Example:
        >>> bg = BaseGeometry()
        >>> bg.area()
        Traceback (most recent call last):
            ...
        Exception: area() is not implemented
    """

    def area(self):
        """
        Compute the area of a geometric shape.

        This method is intended to be overridden in derived classes.
        Calling it directly will raise an Exception.

        Raises:
            Exception: If called without being implemented in a subclass.
        """
        raise Exception("area() is not implemented")
