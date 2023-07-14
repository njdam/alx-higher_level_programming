#!/usr/bin/python3
"""A file defines a class Student which define a student."""


class Student:
    """A class Student which define a student."""

    def __init__(self, first_name, last_name, age):
        """Initialisation of class Student with first and last name and age

        Args:
            first_name (str): is a first name of a student.
            last_name (str): is a last name of a student.
            age (int): is an age of a student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A function to get dictionary represantation of a student."""

        return (self.__dict__)
