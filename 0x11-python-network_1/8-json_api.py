#!/usr/bin/python3
"""
A Python script that sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter and processes the JSON response.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": letter}

    try:
        response = requests.post(url, data=data)
        response_data = response.json()

        if response_data:
            print("[{}] {}".format(response_data['id'], response_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
