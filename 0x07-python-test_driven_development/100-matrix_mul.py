#!/usr/bin/python3
"""
This module contains a function that multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: Result of matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists.
        ValueError: If m_a or m_b is empty, or matrices cannot be multiplied.
        TypeError: If m_a or m_b contains elements other than integers or floats.
        TypeError: If rows of m_a or m_b are not of the same size.

    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError(
            "m_a must be a list of lists or m_b must be a list of lists")

    if m_a == [] or any(row == [] for row in m_a) or m_b == [] or any(row == [] for row in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or \
       not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError(
            "m_a should contain only integers or floats or m_b should contain only integers or floats")

    if len(set(len(row) for row in m_a)) != 1 or len(set(len(row) for row in m_b)) != 1:
        raise ValueError(
            "each row of m_a must be of the same size or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    num_rows_a = len(m_a)
    num_cols_a = len(m_a[0])
    num_cols_b = len(m_b[0])

    result = [[0 for _ in range(num_cols_b)] for _ in range(num_rows_a)]

    for i in range(num_rows_a):
        for j in range(num_cols_b):
            for k in range(num_cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
