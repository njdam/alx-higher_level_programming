#!/usr/bin/python3
"""
    A Python script that takes 2 arguments in order to retrieve the last 10
    commits of a repository of an owner given.

    Usage: ./100-github_commits.py repo_name owner_name
"""

from sys import argv
import requests


if __name__ == '__main__':
    if len(argv) > 2:
        # Variable and Arguments declaration
        repo_name = argv[1]
        owner_name = argv[2]
        api = "https://api.github.com"

        # Request url for commits of a given repository and owner
        request = "{}/repos/{}/{}/commits?{}".format(
                api,
                owner_name,
                repo_name,
                "per_page=10"
                )

        # Requesting and retrieving the request results
        response = requests.get(
                request,
                headers={"Accept": "application/vnd.github.v3+json"}
                )

        # If status code is Ok (200) get sha number and author to be printed
        if response.status_code == 200:
            for commit in response.json():
                commit_hash = commit['sha']
                commit_author_name = commit["commit"]["author"]["name"]
                print("{}: {}".format(commit_hash, commit_author_name))
