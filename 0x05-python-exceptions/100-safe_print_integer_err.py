#!/usr/bin/pyhton3
# A function to an integer.

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as TVErr:
        print("Exception: {}".format(TVErr), file=sys.stderr)
        return (False)
