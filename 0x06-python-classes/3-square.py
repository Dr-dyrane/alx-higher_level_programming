#!/usr/bin/python3
# 3-square.py
# Alexander Udeogarahnya <Ogranya.Alex@gmail.com>
"""Define a class Square."""


class Square:
    """
    Represent a square.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new square. Default is 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
