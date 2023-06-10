#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """
    This is the BaseGeometry class.

    Attributes:
        None

    Methods:
        area(self): Raises an Exception with the message "area() is not implemented"
        integer_validator(self, name, value): Validates the value as an integer.
    """
    def area(self):
        """
        This method raises an Exception indicating that area() is not implemented.

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


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle object with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The rectangle description in the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
