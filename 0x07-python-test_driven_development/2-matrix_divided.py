def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    This function ensures that:
    - The input matrix is a list of lists containing only integers or floats.
    - All rows in the matrix are of the same length.
    - The divisor `div` is a number (int or float).
    - The divisor is not zero.

    Args:
        matrix (list of list of int/float): The matrix to be divided.
        div (int/float): The number to divide each element of the matrix by.

    Returns:
        list: A new matrix with each element divide
        d by `div`, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of numbers.
        TypeError: If the rows of the matrix are not of equal length.
        TypeError: If `div` is not a number.
        ZeroDivisionError: If `div` is zero.

    Examples:
        >>> matrix_divided([[4, 8], [16, 32]], 2)
        [[2.0, 4.0], [8.0, 16.0]]

        >>> matrix_divided([[1.5, 3.2], [5.6, 7.8]], 2)
        [[0.75, 1.6], [2.8, 3.9]]

        >>> matrix_divided([[10, 20, 30], [40, 50, 60]], 10)
        [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

        >>> matrix_divided([[1, 2, 3], [4, 5]], 2)
        Traceback (most recent call last):
        ...
        TypeError: Each row of the matrix must have the same size

        >>> matrix_divided([[1, 2], ["a", 4]], 2)
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
         (not all(isinstance(row, list) for row
                  in matrix)) or
         (not all(isinstance(num, (int, float)) fo
                  row in matrix for num in row)))):
        raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")

    # Validate that all rows have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate `div`
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
