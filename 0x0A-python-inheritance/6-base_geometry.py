#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """
    This is the BaseGeometry class.

    Attributes:
        None

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented"
    """
    def area(self):
        """
        This method raises an Exception indicating that area() is not implemented.

        Raises:
            Exception: Raised with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
