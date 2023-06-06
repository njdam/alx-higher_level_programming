#!/usr/bin/python3
# printing number from 0 to 99 separated by comma and space.
for num in range(100):
    if num == 99:
        print("{}".format(num))
    else:
        print("{:02}".format(num), end=", ")
