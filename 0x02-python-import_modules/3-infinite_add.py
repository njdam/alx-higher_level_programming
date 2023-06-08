#!/usr/bin/python3
# This is the script to add all command line arguments

if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    result = 0

    if argc == 0:
        print("{}".format(result))

    else:
        for i in range(1, argc):
            num = int(argv[i])
            result += num

        print("{}".format(result))
