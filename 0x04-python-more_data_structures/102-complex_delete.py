#!/usr/bin/python3
# A function to delete a key with a specific value in a dictionary.


def complex_delete(a_dictionary, value):
    del_keys = [key for key, val in a_dictionary.items() if val == value]
    for key in del_keys:
        del a_dictionary[key]

    return (a_dictionary)
