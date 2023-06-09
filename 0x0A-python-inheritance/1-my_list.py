#!/usr/bin/python3
"""
Contains the MyList class
"""


class MyList(list):
    """
    A subclass of list.

    Attributes:
        No additional attributes.

    Methods:
        __init__(): Initializes the object.
        print_sorted(): Prints the list in sorted (ascending) order.
    """

    def __init__(self):
        """
        Initializes the MyList object.

        Returns:
            None
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)
