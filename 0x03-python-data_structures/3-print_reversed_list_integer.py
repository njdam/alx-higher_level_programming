#!/usr/bin/python3
# A function to print every integer in newline from reversed list.


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
