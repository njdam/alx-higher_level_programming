#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status."""

from urllib import request


if __name__ == '__main__':
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        if response.readable():
            info = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(info)))
            print("\t- content: {}".format(info))
            print("\t- utf8 content: {}".format(info.decode("utf-8")))
