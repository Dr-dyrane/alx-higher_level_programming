#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id header in the response.
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from command-line arguments

    with urllib.request.urlopen(url) as response:
        # Check if the 'X-Request-Id' header is present in the response
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(x_request_id)
