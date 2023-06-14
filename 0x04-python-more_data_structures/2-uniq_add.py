#!/usr/bin/python3
# A function to add all unique integers in a list.

def uniq_add(my_list=[]):
    new_list = set(my_list)  # To remain with unique integers
    result = 0

    for x in new_list:
        result += x

    return (result)
