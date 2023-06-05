
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list): First matrix as a list of lists.
        m_b (list): Second matrix as a list of lists.

    Returns:
        list: Resulting matrix as a list of lists.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists.
        ValueError: If m_a or m_b is empty or the matrices cannot be multiplied.

    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError(
            "m_a must be a list of lists and m_b must be a list of lists")

    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty and m_b can't be empty")

    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")

    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")

    try:
        np_m_a = np.array(m_a)
        np_m_b = np.array(m_b)
        result = np.matmul(np_m_a, np_m_b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
