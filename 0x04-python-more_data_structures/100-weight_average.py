#!/usr/bin/python3
# A function to return a weighted average of all integers tuple.


def weight_average(my_list=[]):
    if not my_list:
        return (0)

    result = 0
    lens = 0
    for y in my_list:
        result += (y[0] * y[1])
        lens += y[1]

    final = result / lens
    return (final)
