#!/usr/bin/pyhton3
# A function to find and return a largest integer in a list.


def max_integer(my_list=[]):
    #lens = len(my_list)

    if len(my_list) == 0:
        return (None)
    
    num = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > num:
            num = my_list[i]

    return (num)
