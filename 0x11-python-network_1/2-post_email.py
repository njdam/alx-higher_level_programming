#!/usr/bin/python3
"""A Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    if len(argv) > 2:
        dec_data = bytes(parse.urlencode([('email', argv[2])]), 'utf-8')
        with request.urlopen(argv[1], data=dec_data) as response:
            print(response.read().decode('utf-8'))
