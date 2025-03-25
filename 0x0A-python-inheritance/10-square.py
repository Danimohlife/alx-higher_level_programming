#!/usr/bin/python3
"""
Module containing the Square class, which inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The side length of the square.
            Must be a positive integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square (size * size).

        Example:
            >>> s = Square(5)
            >>> s.area()
            25
        """
        return self.__size ** 2
    '''

    def __str__(self):
        """
        Returns the string representation of the square.

        Returns:
            str: A formatted string representation of the square.

        Example:
            >>> s = Square(5)
            >>> print(s)
            [Square] 5/5
        """
        return f"[Square] {self.__size}/{self.__size}"
    '''
