#!/usr/bin/python3
# A function to print x elements of a list

def safe_print_list(my_list=[], x=0):
    rval = 0
    for i in range(x):
        try:
            value = my_list[i]
        except IndexError:
            break
        else:
            rval += 1
            print("{}".format(my_list[i]), end="")
    print("")

    return (rval)
