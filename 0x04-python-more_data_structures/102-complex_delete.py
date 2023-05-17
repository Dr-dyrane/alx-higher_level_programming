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
    keys_to_del = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_to_del:
        del a_dictionary[key]
    return a_dictionary
