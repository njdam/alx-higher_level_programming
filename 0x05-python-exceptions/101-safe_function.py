#!/usr/bin/python3
# A function to return result by a function to two args.


def safe_function(fct, *args):
    import sys
    result = None

    try:
        result = fct(*args)
        return (result)

    except Exception as AnyErr:
        print("Exception: {}".format(AnyErr), file=sys.stderr)
        return (result)
