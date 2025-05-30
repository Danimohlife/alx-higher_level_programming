#!/usr/bin/python3
"""
class Square  with impliment of compare operator.


this enable comparism of instance to instance
or Object to Object
"""


class Square:
    """A class that defines a square with size and comparison capabilities."""

    def __init__(self, size=0):
        """
        Initializes a square.

        Args:
            size (int or float): The size of the square (must be >= 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int or float): The new size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if two squares have equal area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks if two squares have different areas."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Checks if the current square is greater than another."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if the current square is greater than or equal to another."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Checks if the current square is less than another."""
        return self.area() < other.area()

    def __le__(self, other):
        """Checks if the current square is less than or equal to another."""
        return self.area() <= other.area()
