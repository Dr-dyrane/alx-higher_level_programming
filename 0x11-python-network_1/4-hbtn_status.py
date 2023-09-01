#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
using the requests library
and displays the response body with type information.
"""

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    # Send a GET request to the URL
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
