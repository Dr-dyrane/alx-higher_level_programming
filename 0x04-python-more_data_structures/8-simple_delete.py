#!/usr/bin/python3

# Function that deletes a key in a dictionary
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Arguments:
    a_dictionary -- The dictionary from which the key will be deleted.
    key -- The key to be deleted. (default: "")

    Returns:
    The updated dictionary.
    """
    a_dictionary.pop(key, None)
    return a_dictionary
