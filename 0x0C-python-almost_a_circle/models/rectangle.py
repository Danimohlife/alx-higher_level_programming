#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from Base.
"""

from models.base import Base


class Rectangle(Base):
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        y (int): The y-coordinate of the rectangle.
        id (int): The identifier of the instance.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate. Defaults to 0.
            y (int, optional): The y-coordinate. Defaults to 0.
            id (int, optional): The identifier. Defaults to None.
        """
        super().__init__(id)  # Call Base constructor
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x with validation."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y with validation."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area to calculate the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """
        print out the # rep of rectangle
        """
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """
        string representation of Rectangle
        """
        d = self.id
        w = self.__width
        h = self.__height
        return f"[Rectangle] ({d}) {self.__x}/{self.__y} - {w}/{h}"

    def update(self, *args):
        """
        Updates attributes in order of: id, width, height, x, y.
        Args:
            *args: Variable length argument list to update attributes.
        """
        attributes = ["id", "width", "height", "x", "y"]
        for i, value in enumerate(args):
            if i < len(attributes):
                setattr(self, attributes[i], value)
