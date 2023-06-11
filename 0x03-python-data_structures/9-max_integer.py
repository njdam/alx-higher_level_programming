#!/usr/bin/pyhton3
# A function to find and return a maximum integer in a list.


def max_integer(my_list=[]):
    lens = len(my_list)

    if lens == 0:
        return ("None")

    else:
        maxim = 0
        for i in range(lens - 1):
            if my_list[i] < my_list[i + 1] and my_list[i + 1] > maxim:
                maxim = my_list[i + 1]

            elif my_list[i] > maxim:
                maxim = my_list[i]

        return (maxim)
