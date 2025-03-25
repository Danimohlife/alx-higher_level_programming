#!/usr/bin/python3
"""
Module: my_list

This module defines a subclass `MyList` that extends the built-in `list` class.
It provides an additional method to print the list in sorted order.
"""


class MyList(list):
    """
    A subclass of the built-in `list` that includes a method to print
    the list in ascending sorted order.

    Methods:
        print_sorted():
            Prints the elements of the list in ascending sorted order.

    Example:
        >>> my_list = MyList([3, 1, 4, 2])
        >>> my_list.print_sorted()
        [1, 2, 3, 4]
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order.

        This method does not modify the original list.

        Example:
            >>> my_list = MyList([5, 2, 9, 1])
            >>> my_list.print_sorted()
            [1, 2, 5, 9]
        """
        print(sorted(self))
