#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list of lists: A new matrix with the divided elements
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
                   If any row of the matrix has a different size
                        than the others.
                   If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_sizes = [len(row) for row in matrix]
    if len(set(row_sizes)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row]
                  for row in matrix]
    return new_matrix
