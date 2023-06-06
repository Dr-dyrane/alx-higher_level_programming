#!/usr/bin/python3
"""
This module provides a function to generate a magic string.
"""


def magic_string(H=[]):
    """
    Generates a magic string "BestSchool" n times the number of iterations.

    Args:
        H (list): The list to store the magic string.

    Returns:
        str: The magic string.
    """
    H += ["BestSchool"]
    return ", ".join(H)
