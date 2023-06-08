#!/usr/bin/python3
# A program to import and handle basic mathematical operations

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    exit = sys.exit

    argc = len(argv) - 1  # To remove count for a program

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = {"+": add, "-": sub, "*": mul, "/": div}  # Allowed operators
    b = int(argv[3])

    if argv[2] not in list(op.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = op[argv[2]](a, b)
    print("{} {} {} = {}".format(a, argv[2], b, result))
