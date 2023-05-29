#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for ai in range(x):
        try:
            print(my_list[ai], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
