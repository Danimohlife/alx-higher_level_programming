#!/usr/bin/python3
"""
Module: square

This module defines a Square class with size validation,
position handling, and printing functionalities.
"""


class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): The size of the square (private).
        __position (tuple): The position of
        the square when printed.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with size and position.

        Args:
            size (int, optional): The size of the
            square. Defaults to 0.
            position (tuple, optional): The position
            (x, y). Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or
            position is not a tuple of two positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square,
        ensuring it's a non-negative integer.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The (x, y) position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square,
        ensuring it's a tuple of two non-negative
        integers.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a
            tuple of two non-negative integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(_, int) for _ in value) or
                not all(_ >= 0 for _ in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size^2).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character,
        considering its position.

        If size is 0, an empty line is printed.

        The `position` attribute controls the
        horizontal and vertical spacing.
        """
        if self.__size == 0:
            print()
            return

        # Print vertical spacing based on position[1]
        for _ in range(self.__position[1]):
            print()

        # Print the square with position[0] spaces
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns the string representation of the square
        """

        if self.__size == 0:
            return ""

        square_str = "\n" * self.__position[1]

        for i in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size
            if i < self.__size - 1:
                square_str += "\n"

        return square_str
