#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

from sys import argv
import requests


if __name__ == '__main__':
    query = argv[1] if len(argv) > 1 else ""
    dec_data = [('q', query)]
    url = "http://0.0.0.0:5000/search_user"
    responses = requests.post(url, data=dec_data)
    try:
        json_content = responses.json()
        if json_content:
            print('[{}] {}'.format(json_content['id'], json_content['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
