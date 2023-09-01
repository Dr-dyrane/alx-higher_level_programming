#!/usr/bin/python3
"""
A Python script that uses GitHub API to display your GitHub user ID.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    auth = (username, token)

    try:
        response = requests.get(url, auth=auth)
        user_data = response.json()
        if 'id' in user_data:
            print(user_data['id'])
        else:
            print("None")
    except ValueError:
        print("None")
