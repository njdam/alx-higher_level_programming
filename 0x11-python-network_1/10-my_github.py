#!/usr/bin/python3
"""A Python script to take your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

from sys import argv
import requests


if __name__ == '__main__':
    if len(argv) > 2:
        request_headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Username': argv[1],
            'Authorization': 'token {}'.format(argv[2]),
        }
        url = "https://api.github.com/user"
        responses = requests.get(url, headers=request_headers)
        if responses.status_code == 200:
            user = responses.json()
            username = argv[1]
            if user['login'] == username:
                print(user['id'])
            else:
                print('None')
        else:
            print('None')
