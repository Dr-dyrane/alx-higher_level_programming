#!/usr/bin/python3
"""
This is the "4-print_square" module.
The 4-print_square module supplies one function, print_square(size).
"""


def print_square(size):
    """
    Prints a square with '#' characters of the given size.

    Args:
        size (int): The length of the square.

    Raises:
        TypeError: If size is not an integer or float.
        ValueError: If size is less than 0 or a float less than 0.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size > 0:
        for _ in range(size):
            print("#" * size)
