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
        area(self): Exception with the message "area() is not implemented"
        integer_validator(self, name, value): Validates the value as integer.
    """
    def area(self):
        """
        This method raises an Exception.

        Raises:
            Exception: Raised with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates the value as an integer.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Example:
            bg = BaseGeometry()
            bg.integer_validator("my_int", 12)  # Valid
            bg.integer_validator("width", 89)  # Valid
            bg.integer_validator("name", "John")  # Raises TypeError
            bg.integer_validator("age", 0)  # Raises ValueError
            bg.integer_validator("distance", -4)  # Raises ValueError
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
