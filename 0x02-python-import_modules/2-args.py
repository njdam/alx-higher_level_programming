#!/usr/bin/python3
""" this the script to print all command line arguments, one by one
and started by it's index number.
"""
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1  # to remove program non accessable index

    if argc == 0:
        print("{} arguments.".format(argc))

    else:
        if argc == 1:
            print("{} argument:".format(argc))
        else:
            print("{} arguments:".format(argc))

        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
