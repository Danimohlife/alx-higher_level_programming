#!/usr/bin/python3
"""
This module provides a function `matrix_divided` that divides
all elements of a matrix by a given number.

Functions:
    - matrix_divided(matrix, div): Returns a new matrix where
      each element is divided by `div` and rounded to 2 decimal places.

Raises:
    - TypeError: If the matrix is not a list of lists of numbers.
    - TypeError: If the rows of the matrix are not of equal length.
    - TypeError: If `div` is not a number.
    - ZeroDivisionError: If `div` is zero.

Example Usage:
    >>> matrix = [[10, 20], [30, 40]]
    >>> matrix_divided(matrix, 10)
    [[1.0, 2.0], [3.0, 4.0]]

Author: Your Name (Replace with yours)
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Ensures:
    - The input `matrix` is a list of lists containing only integers or floats.
    - All rows in the matrix are of the same length.
    - The divisor `div` is a number (int or float).
    - The divisor is not zero.

    Args:
        matrix (list of list of int/float): The matrix to be divided.
        div (int/float): The number to divide each element of the matrix by.

    Returns:
        list: A new matrix with each element
        divided by `div`, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of numbers.
        TypeError: If the rows of the matrix are not of equal length.
        TypeError: If `div` is not a number.
        ZeroDivisionError: If `div` is zero.

    Examples:
        >>> matrix_divided([[4, 8], [16, 20]], 4)
        [[1.0, 2.0], [4.0, 5.0]]

        >>> matrix_divided([[3, 6], [9, 12]], 3)
        [[1.0, 2.0], [3.0, 4.0]]

        >>> matrix_divided([[1.5, 3.0], [4.5, 6.0]], 1.5)
        [[1.0, 2.0], [3.0, 4.0]]

        >>> matrix_divided([[10, 20, 30], [40, 50, 60]], 10)
        [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

        >>> matrix_divided([[7, 14], [21, 28]], 7)
        [[1.0, 2.0], [3.0, 4.0]]

        >>> matrix_divided([[1, 2], [3, "4"]], 2)
        Traceback (most recent call last):
            ...
        TypeError: matrix must be a matrix (list of lists) of integers/floats

        >>> matrix_divided([[1, 2], [3, 4, 5]], 2)
        Traceback (most recent call last):
            ...
        TypeError: Each row of the matrix must have the same size

        >>> matrix_divided("not a matrix", 2)
        Traceback (most recent call last):
            ...
        TypeError: matrix must be a matrix (list of lists) of integers/floats

        >>> matrix_divided([[1, 2], [3, 4]], "2")
        Traceback (most recent call last):
            ...
        TypeError: div must be a number

        >>> matrix_divided([[1, 2], [3, 4]], 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero
    """

    if ((not isinstance(matrix, list) or
         not all(isinstance(row, list) for row in matrix) or
         not all(isinstance(num, (int, float)) for
                 row in matrix for num in row))):
        raise TypeError("matrix must be a matrix \
                (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
