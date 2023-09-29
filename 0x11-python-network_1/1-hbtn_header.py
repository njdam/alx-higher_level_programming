#!/usr/bin/python3
"""A Python script to take in a URL, sends a request to the URL and displays
the value of X-Request-Id variable found in the header of the response.
"""

from sys import argv
from urllib import request


if __name__ == '__main__':
    if len(argv) > 1:
        with request.urlopen(argv[1]) as response:
            url_id = response.headers['X-Request-Id']
            print(url_id)
