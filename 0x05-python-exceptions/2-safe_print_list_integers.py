#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ai = 0
    for ja in range(x):
        try:
            print("{:d}".format(my_list[ja]), end="")
            ai += 1
        except(ValueError, TypeError):
            continue
    print()
    return ai
