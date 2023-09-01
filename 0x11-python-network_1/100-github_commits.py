#!/usr/bin/python3
"""
A Python script to list 10 most recent commits of a GitHub repository.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository> <owner>")
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    params = {
        'per_page': 10,
    }

    try:
        response = requests.get(url, params=params)
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except ValueError:
        print("Could not retrieve commits")
