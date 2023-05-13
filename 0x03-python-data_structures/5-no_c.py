#!/usr/bin/python3
def no_c(my_string):
    no_c_str = ""
    str_copy = list(my_string)
    for i in range(len(my_string)):
        if my_string[i] == 'c':
            str_copy.remove('c')
        if my_string[i] == 'C':
            str_copy.remove('C')
    return no_c_str.join(str_copy)
