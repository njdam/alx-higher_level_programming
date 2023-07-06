#!/usr/bin/python3
"""A file containing a class Rectangle which defines rectangle."""


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
        self.width = width  # width becames the first for __dict__ call
        self.height = height  # height becames the second for __dict__ call

    @property
    def width(self):
        """A function to retrieve a value of width."""
        return self.__width

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
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """A function to return area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """A function to return parameter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)

        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """A function to return bigger rectangle

        Paramenetrs:
            rect_1 (Rectangle): is the first rectangle.
            rect_2 (Rectangle): is the second rectangle.
        Raise:
            TypeError: if either rect_1 or rect_2 is not a rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)

        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle as square with size equal to size.

        Args:
            size (int): is equal to width and height of new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """A function to return printable represantation of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for y in range(self.__height):
            for x in range(self.__width):
                rectangle.append(str(self.print_symbol))

            if y != self.__height - 1:
                rectangle.append("\n")

        return ("".join(rectangle))

    def __repr__(self):
        """Function to return string representation to create rectangle."""
        recr = "Rectangle(" + str(self.__width)
        recr += ", " + str(self.__height) + ")"

        return (recr)

    def __del__(self):
        """A function to print a messange if rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
