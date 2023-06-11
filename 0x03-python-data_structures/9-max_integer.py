#!/usr/bin/pyhton3
# A function to find and return a largest integer in a list.


def max_integer(my_list=[]):
    lens = len(my_list)

    if lens == 0:
        return (None)

    else:
        maxim = my_list[0]
        for i in range(lens):
            if my_list[i] > maxim:
                maxim = my_list[i]

        return (maxim)
