#!/usr/bin/pyhton3
# A function to find and return a largest integer in a list.


def max_integer(my_list=[]):
    lens = len(my_list)

    if lens == 0:
        return ("None")

    else:
        num = 0
        for i in range(lens - 1):
            if my_list[i] < my_list[i + 1] and my_list[i + 1] > num:
                num = my_list[i + 1]

            elif my_list[i] > num:
                num = my_list[i]

        return (num)
