#!/usr/bin/pyhton3
# A function to an integer.

def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as TVErr:
        print("Exception: {}".format(TVErr), file=sys.stderr)
        return (False)
