#!/usr/bin/python3
# A function to return a set of common elements in two sets.


def common_elements(set_1, set_2):
    c_set = []
    for y in set_1:
        for x in set_2:
            if y[:] == x[:]:
                c_set.append(x)

    return (c_set)
