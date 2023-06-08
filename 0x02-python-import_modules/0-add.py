#!/usr/bin/python3
# A script to import add function from it file.py to print sum of a and b

if __name__ == '__main__':
    from add_0 import add
    a = 1
    b = 2
    print("{} {} {} {} {}".format(a, "+", b, "=", add(a, b)))
