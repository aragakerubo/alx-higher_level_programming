#!/usr/bin/python3
"""
Script that takes 2 arguments in order to solve this challenge
"""

import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get("sha")
        commit = commit.get("commit")
        author = commit.get("author")
        name = author.get("name")
        print("{}: {}".format(sha, name))
