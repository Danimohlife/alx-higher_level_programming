#!/usr/bin/python3
"""
Module containing the Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle and inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            Must be a positive integer.
            height (int): The height of the rectangle.
            Must be a positive integer.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        super().integer_validator("width", width)  # Validate width
        self.__width = width
        super().integer_validator("height", height)  # Validate height
        self.__height = height

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).

        Example:
            >>> r = Rectangle(4, 5)
            >>> r.area()
            20
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Returns:
            str: A formatted string representation of the rectangle.

        Example:
            >>> r = Rectangle(4, 5)
            >>> print(r)
            [Rectangle] 4/5
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
