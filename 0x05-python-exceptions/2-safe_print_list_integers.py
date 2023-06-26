#!/usr/bin/python3
# A function to print integers in x elements from my_list elements

def safe_print_list_integers(my_list=[], x=0):
    rval = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            rval += 1
        except (ValueError, TypeError):
            pass
    print("")
    return (rval)
