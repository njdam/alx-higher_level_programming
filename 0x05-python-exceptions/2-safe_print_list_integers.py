#!/usr/bin/python3
# A function to print integers in x elements from my_list elements

def safe_print_list_integers(my_list=[], x=0):
    rval = 0
    for i in range(x):
        try:
            value = int(my_list[i])
        except (IndexError, ValueError, TypeError):
            continue
        else:
            rval += 1
            print("{:d}".format(value), end="")
    print("")
    return (rval)
