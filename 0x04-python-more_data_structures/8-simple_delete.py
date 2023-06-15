#!/usr/bin/python3
# A function to delete a key in a dictionary if present otherwise not.


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]

    return (a_dictionary)
