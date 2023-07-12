#!/usr/bin/python3
"""A file with empty class called BaseGeometry."""


class BaseGeometry:
    """An empty class called BaseGeometry."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validate a value if is an integer.

        Args:
            name (str): is always a string
            value (int): must be an integer.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
