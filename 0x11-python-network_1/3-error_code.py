#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).

It handles urllib.error.HTTPError exceptions and prints the
HTTP status code if an error occurs.
"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from command-line arguments

    try:
        # Send a request to the URL and get the response
        with urllib.request.urlopen(url) as response:
            # Decode and print the response body
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        # Handle HTTPError exceptions by printing the HTTP status code
        print("Error code:", e.code)
