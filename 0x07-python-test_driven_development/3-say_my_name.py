#!/usr/bin/python3
"""A function to say my both first name and last name."""


def say_my_name(first_name, last_name=""):
    """A `say_my_name` function to say my name

    Parameters:
        first_name (str): is my first name and must be a string
        last_name (str): is my last name and must be a string

    Raises:
        TypeError: if either first_name or last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(first_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
