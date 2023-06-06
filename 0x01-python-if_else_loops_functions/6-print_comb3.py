#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if x < y and x != 8:
            print("{}{}".format(x, y), end=", ")
        elif x < y and x == 8:
            print("{}{}".format(x, y))
