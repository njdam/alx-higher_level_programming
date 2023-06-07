#!/usr/bin/python3
for al in range(122, 96, -1):
    x = abs(al) % 2
    if (x != 0):
        al = al - 32
    print("{}".format(chr(al)), end="")
