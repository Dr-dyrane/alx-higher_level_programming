#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to perform deletion on.
        value: The specific value to search for and delete keys.

    Returns:
        dict: The modified dictionary after deleting keys.
    """
    return {key: val for key, val in a_dictionary.items() if val != value}
