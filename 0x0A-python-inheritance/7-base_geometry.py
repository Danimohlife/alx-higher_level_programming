#!/usr/bin/python3
"""
aseGeometry:
    A base class for geometry operations.
    Raises an Exception because area() is not implemented."""


class BaseGeometry:
    """
    Raises an Exception because area() is not implemented
    Raises an Exception because area() is not implemented.
    """
    def area(self):
        """
        Raises an Exception because area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that `value` is a positive integer.

        Args:
            name (str): Name of the variable.
            value (int): Value to validate.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is not greater than zero.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
