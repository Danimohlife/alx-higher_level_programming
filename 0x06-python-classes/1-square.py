#!/usr/bin/python3
"""
Module: square

This module defines a Square class with an instantiation of size
without type verification.
"""


class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size: The size of the square (no type verification).
        """
        self.__size = size
