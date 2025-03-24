class Rectangle:
    """
    A class that defines a rectangle with width and height.

    Attributes:
        number_of_instances (int): Tracks the number of active instances.
        print_symbol (any): Symbol used for
        string representation of the rectangle.
    """

    number_of_instances = 0  # Tracks active instances
    print_symbol = "#"  # Default symbol for printing the rectangle

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle (default is 0).
            height (int, optional): The height of the rectangle (default is 0).

        Increments the `number_of_instances` class attribute on instantiation.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment instance count

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Determines the larger rectangle based on area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the larger area.
            If both have the same area, returns `rect_1`.

        Raises:
            TypeError: If `rect_1` is not an instance of Rectangle.
            TypeError: If `rect_2` is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
