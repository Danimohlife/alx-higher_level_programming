#!/usr/bin/python3
"""
Module for defining a Rectangle class.

This module provides a `Rectangle` class that allows the creation of
rectangle objects with width and height attributes. It includes property
methods for attribute validation.
"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).

    Properties:
        width: Getter and setter for the rectangle's
        width, ensuring it's a non-negative integer.
        height: Getter and setter for the rectangle's
        height, ensuring it's a non-negative integer.

    Methods:
        __init__(self, width=0, height=0):
            Initializes a rectangle with optional width and height values.

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is negative.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        self.width = width
        self.height = height
        number_of_instances += 1

    @property
    def width(self):
        """
        Getter for the width of the rectangle.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        The area of a rectangle is computed as:
            area = width * height

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        The perimeter of a rectangle is computed as:
            perimeter = 2 * (width + height)

        If either width or height is 0, the perimeter is defined as 0.

        Returns:
            int: The perimeter of the rectangle, or 0 if either dimension is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of
        the rectangle using the '#' character.

        If either the width or height is 0, an empty string is returned.

        The rectangle is represented as a series
        of rows, where each row contains
        `width` number of '#' characters, and
        there are `height` number of rows.

        Returns:
            str: A string representation of the rectangle, where '#' represents
            each unit, with rows separated by newlines.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        return "\n".join(['#' * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string representation of the Rectangle instance
        that can be used to recreate the object using eval().

        The string follows the format:
        "Rectangle(width, height)"

        Returns:
            str: A string representation of the Rectangle instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when a Rectangle instance is deleted.

        This method is automatically called when the instance is
        about to be destroyed, such as when `del` is used or when
        it goes out of scope.

        Example:
        """
        number_of_instances -= 1
        print("Bye rectangle...")
