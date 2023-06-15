#!/usr/bin/python3
# A function that return a new dictionary with value multiplied by 2.


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key in new_dict:
        new_dict[key] *= 2

    return (new_dict)
