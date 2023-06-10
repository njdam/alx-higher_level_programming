#!/usr/bin/python3
# A function to delete a letter in a string to return new one.


def no_c(my_string):
    new_string = [c for c in my_string if ord(c) != 67 and ord(c) != 99]
    return ("".join(new_string))
