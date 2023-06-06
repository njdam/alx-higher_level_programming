#!/usr/bin/python3
def uppercase(str):
    for al in str:
        x = ord(al)
        if x > 96 and x < 123:
            al = chr(x - 32)
        print("{}".format(al), end="")

    print("")
