#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """
    Computes the square value of all integers in a matrix using map.

    Args:
        matrix (list): The 2-dimensional array.

    Returns:
        list: The new matrix with each value squared.
    """
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
