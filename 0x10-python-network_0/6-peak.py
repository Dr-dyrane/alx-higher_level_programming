#!/usr/bin/python3
"""
This module contains a function that
finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Finds peaks in a list of unsorted integers.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        list: A list of peak elements. Returns an empty list if the input list is empty.
    """
    peaks = []

    if not list_of_integers:
        return peaks

    low = 0
    high = len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2

        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            peaks.append(list_of_integers[mid])
        
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return peaks
