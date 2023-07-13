#!/usr/bin/python3
"""A script to read stdin line by line and computes metrics,
for every ten lines or keyboard interruption by CTRL + C prints:
    => Total file size: `File size: <total size>` upto that point
    => Number of lines by status code upto that point.
"""


def print_status(size, status_codes):
    """A function to print accumulated metrics.

    Args:
        size (int): is the size of accumulated read file,
        status_codes (dict): is a dict with accumulated ct of status codes.
    """

    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    """Main functions for calling our functions."""

    import sys

    size = 0
    status = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    num_line = 0

    try:
        for line in sys.stdin:
            if num_line == 10:  # If lines are equal to 10 lines.
                print_status(size, status)
                num_line = 1
            else:
                num_line += 1

            line = line.split()

            try:
                size += int(line[-1])  # for Indentation and Value Error

            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:  # For valid codes
                    if status.get(line[-2], -1) == -1:
                        status[line[-2]] = 1
                    else:
                        status[line[-2]] += 1

            except IndexError:  # for Indentation Error
                pass

        print_status(size, status)

    except KeyboardInterrupt:  # For keyboard interruption by Ctrl + C
        print_status(size, status)
        raise
