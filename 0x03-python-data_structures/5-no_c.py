#!/usr/bin/python3
# A function to delete a letter in a string to return new one.


def no_c(my_string):
    new_string = [char for char in my_string if ord(char) != 67 and ord(char) != 99]
    return ("".join(new_string))
