#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        if c > b:
            return c
        else:
            return a + b
    else:
        return a * b - c
