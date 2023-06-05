#!/usr/bin/python3
"""This module contains a function that multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices and return the resulting matrix.
    """

    validate_matrix(m_a, "m_a")
    validate_matrix(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []

    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            row.append(sum)
        result.append(row)

    return result


def validate_matrix(matrix, name):
    """
    Validate the given matrix according to the requirements.
    """

    if not isinstance(matrix, list):
        raise TypeError("{} must be a list".format(name))

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("{} must be a list of lists".format(name))

    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise ValueError("{} can't be empty".format(name))

    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(
                "{} should contain only integers or floats".format(name))

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("each row of {} must be of the same size".format(name))
