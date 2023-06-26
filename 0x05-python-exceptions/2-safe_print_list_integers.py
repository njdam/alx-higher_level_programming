#!/usr/bin/python3
# A function to print integers in x elements from my_list elements

def safe_print_list_integers(my_list=[], x=0):
    rval = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                rval += 1
    except (IndexError, ValueError, TypeError):
        pass
    print("")
    return (rval)
