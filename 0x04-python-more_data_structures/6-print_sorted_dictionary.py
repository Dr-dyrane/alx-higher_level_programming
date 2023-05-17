#!/usr/bin/python3
# Function that prints a dictionary by ordered keys
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
