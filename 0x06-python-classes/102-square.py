#!/usr/bin/python3
# 102-square.py
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
            size (float or int): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Check if two squares are equal in size.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the squares are equal in size, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Check if two squares are not equal in size.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the squares are not equal in size, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Check if the current square is smaller than the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the current square is smaller, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Check if the current square is smaller or equal to the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the current square is smaller or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Check if the current square is greater than the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the current square is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Check if the current square is greater or equal to the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            True if the current square is greater or equal, False otherwise.
        """
        return self.area() >= other.area()
