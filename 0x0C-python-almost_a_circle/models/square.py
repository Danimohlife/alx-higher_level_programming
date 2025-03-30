#!/usr/bin/python3
"""Defines the Square class, which inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square, which is a special case of a rectangle.

    Inherits from:
        Rectangle (which in turn inherits from Base).

    Attributes:
        Inherits width, height, x, y, and id from Rectangle.
        Size is defined as both width and height.

    Methods:
        __init__(size, x=0, y=0, id=None) - Initializes a new square.
        __str__() - Returns a string representation of the square.
        size (property) - Gets or sets the size of
        the square (width and height).
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (both width and height).
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The unique identifier. Defaults to None.

        The width and height attributes are set to the same value as size.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Format: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Gets the size of the square (same as width or height)."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square (updates both width and height)."""
        self.width = value
        self.height = value
