#!/usr/bin/python3
# A function to return result by a function to two args.


def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return (result)

    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
