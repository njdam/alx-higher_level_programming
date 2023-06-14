#!/usr/bin/python3
# A function to replace all occurrences of an element by another in a new list.


def search_replace(my_list, search, replace):
    new_list = []
    for x in my_list:
        if x == search:
            x = replace
        new_list.append(x)

    return (new_list)
