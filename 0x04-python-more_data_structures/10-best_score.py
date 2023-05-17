#!/usr/bin/python3

# Function that returns the key with the biggest integer value
def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value in a dictionary.

    Arguments:
    a_dictionary -- The dictionary to search for the best score.

    Returns:
    The key with the biggest integer value, or None if no score found.
    """
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    return None
