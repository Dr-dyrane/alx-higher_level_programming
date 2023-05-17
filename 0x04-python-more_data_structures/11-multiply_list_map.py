#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Returns a new list with all values multiplied by a number using map.

    Args:
        my_list (list): The initial list.
        number (int): The number by which each value in the list will be multiplied.

    Returns:
        list: A new list with all values multiplied by the given number.
    """
    return list(map(lambda x: x * number, my_list))
