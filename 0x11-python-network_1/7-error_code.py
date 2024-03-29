#!/usr/bin/python3
"""A Python script that takes in a URL, sends a request to the URL and
displays the body of the response.
"""

from sys import argv
import requests


if __name__ == '__main__':
    if len(argv) > 1:
        responses = requests.get(argv[1])
        # If responses are in Errors' codes region print Error code
        if responses.status_code >= 400:
            print('Error code: {}'.format(responses.status_code))
        else:
            print(responses.text)
