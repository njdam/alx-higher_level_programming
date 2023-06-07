#!/usr/bin/python3
# a function for fizzbuzz printer

def fizzbuzz():
    for num in range(1, 101):
        n = abs(num)
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz", end=" ")
        elif n % 3 == 0:
            print("Fizz", end=" ")
        elif n % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(num), end=" ")
