#!/usr/bin/python3
"""This file bear a class Base which will be a base of all other classes."""

import json


class Base:
    """A class Base which is a base of all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation of class Base

        Args:
            id (int): is Base class id which is an integer.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A function to return JSON string representation of dictionary."""

        if list_dictionaries is None or not list_dictionaries:
            return ("[]")

        return (json.dumps(list_dictionaries))
