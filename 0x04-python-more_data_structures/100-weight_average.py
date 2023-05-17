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
    if not my_list:
        return 0

    total_score = total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    return total_score / total_weight if total_weight != 0 else 0
