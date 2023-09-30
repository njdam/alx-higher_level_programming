#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == '__main__':
    responses = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(responses.text)))
    print("\t- content: {}".format(responses.text))
