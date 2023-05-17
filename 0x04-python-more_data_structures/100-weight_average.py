#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Returns the weighted average of integers in a list of tuples.

    Args:
        my_list (list): The list of tuples containing (score, weight) pairs.

    Returns:
        float: The weighted average of the integers.
               Returns 0 if the list is empty.
    """
    return sum(score * weight for score, weight in my_list) / sum(weight for _, weight in my_list) if my_list else 0
