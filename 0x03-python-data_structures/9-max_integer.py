#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    for ai in range(len(my_list)):
        if ai == 0:
            largest_num = my_list[ai]
            ai += 1
        if ai < len(my_list) and my_list[ai] > largest_num:
            largest_num = my_list[ai]
    return largest_num
