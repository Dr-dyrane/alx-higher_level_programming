#!/usr/bin/python3

# Function that returns a new dictionary with all values multiplied by 2
def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Arguments:
    a_dictionary -- The dictionary to be multiplied.

    Returns:
    The new dictionary with values multiplied by 2.
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
