#!/usr/bin/python3
# A function to print a dictionary by ordered keys.


def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.keys())  # Soting dictionary by keys.

    for key in sorted_dict:  # Printing according to sorted dictionary.
        print("{}: {}".format(key, a_dictionary[key]))
