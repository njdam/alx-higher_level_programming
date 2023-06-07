#!/usr/bin/python3
# a function to print and return last digit of a number

def print_last_digit(number):
    digit = abs(number) % 10
    print("{}".format(digit), end="")
    return (digit)
