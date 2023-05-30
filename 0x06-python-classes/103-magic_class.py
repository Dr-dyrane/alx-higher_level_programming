#!/usr/bin/python3
# 103-magic_calculation.py
# Alexander Udeogarahnya <Ogranya.Alex@gmail.com>
"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with a given radius.

        Args:
            radius (int or float): The radius of the circle. Default is 0.

        Raises:
            TypeError: If radius is not a number (int or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
