#!/usr/bin/python3
"""A file containing a class `Rectangle` which defines rectangle."""


class Rectangle:
    """A class Rectangle to define a rectangle.

    Attributes:
        number_of_instances (int): is number of Rectangle class instances.
        print_symbol (any): is used as symbol for string represenation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """A function to initialize width and height of a rectangle.

        Arg:
            width (int): is a width of rectangle must be an integer.
            height (int): is a height of rectangle must be an integer.
        """

        type(self).number_of_instances += 1
        self.height = height  # height became the first for call __dict__
        self.width = width  # width became the second for call __dict__

    @property
    def width(self):
        """A function to retrieve a value of width."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """A function to retrieve a value of height."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A function to return area of rectangle."""
        h = self.__height
        w = self.__width

        return (h * w)

    def perimeter(self):
        """A function to return parameter of rectangle."""
        h = self.__height
        w = self.__width
        if self.__width == 0 or self.__height == 0:
            return (0)

        return (2 * (h + w))

    def __str__(self):
        """A function to return printed represantation of rectangle by #."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for y in range(self.__height):
            for x in range(self.__width):
                rectangle.append(str(self.print_symbol))
            if y != (self.__height - 1):
                rectangle.append("\n")

        return ("".join(rectangle))

    def __repr__(self):
        """Function to return string representation to create rectangle."""
        recreation = "Rectangle(" + str(self.__width)
        recreation += ", " + str(self.__height) + ")"

        """Returns rectangle obj in the format `Rectangle(width, height)`"""
        return (recreation)

    def __del__(self):
        """A function to print a messange if rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
