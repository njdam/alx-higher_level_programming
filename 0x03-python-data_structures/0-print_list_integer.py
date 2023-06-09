#!/usr/bin/python3
# A program to print integers in a list one in each line

def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
