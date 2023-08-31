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

    # If the input list is empty, return None
    if not list_of_integers:
        return None

    # Calculate the length of the input list
    length = len(list_of_integers)

    # Calculate the middle index
    mid = length // 2

    # Assign a more descriptive variable name
    integers = list_of_integers

    # Check if the middle element is a peak
    if (mid == 0 or integers[mid] >= integers[mid - 1]) and \
       (mid == length - 1 or integers[mid] >= integers[mid + 1]):
        return integers[mid]

    # If the middle element is smaller than the previous element,
    # search in the left half
    if mid > 0 and integers[mid - 1] > integers[mid]:
        return find_peak(integers[:mid])

    # Otherwise, search in the right half
    return find_peak(integers[mid + 1:])

