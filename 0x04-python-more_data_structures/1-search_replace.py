#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Use a list comprehension to replace elements
    return [replace if element == search else element for element in my_list]
