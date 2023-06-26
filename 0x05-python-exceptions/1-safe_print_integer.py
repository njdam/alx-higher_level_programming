#!/usr/bin/python3
# A function to an integer otherwise exception error

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return (False)
    else:
        return (True)
