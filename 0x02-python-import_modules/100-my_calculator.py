#!/usr/bin/python3
# A program to import and handle basic mathematical operations

if __name__ == "__main__":
    from sys import argv, exit
    argc = len(argv) - 1  # To remove count for a program

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]  # This is operator like +, -, * and /
    b = int(argv[3])

    if len(op) != 1 or op[:1] != ('+' or '-' or '*' or '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    from calculator_1 import add, sub, mul, div
    if op[:1] == "+":
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
        exit(0)

    if op[:1] == "-":
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        exit(0)

    if op[:1] == "*":
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        exit(0)

    if op[:1] == "/":
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
        exit(0)
