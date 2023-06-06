#!/usr/bin/python3
# printing lowercase alphabert except q and e and  followed by newline

for al in range(97, 123):
    if al == 101 or al == 113:
        continue
    print("{}".format(chr(al)), end="")
