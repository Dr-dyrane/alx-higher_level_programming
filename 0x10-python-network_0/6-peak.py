#!/usr/bin/python3
"""
This module contains a function that
finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int or None: The peak element if found, None if the list is empty.
    """

    # Check if the input list is empty, return None if it is
    if not list_of_integers:
        return None

    # Initialize low and high pointers
    low = 0
    high = len(list_of_integers) - 1

    # Perform binary search for the peak
    while low < high:
        mid = (low + high) // 2

        # If the middle element is greater than the next element, move left
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    # The low index now points to a peak element
    return list_of_integers[low]
