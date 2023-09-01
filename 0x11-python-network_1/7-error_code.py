#!/usr/bin/python3
"""
A Python script that sends a request to a URL and
displays the body of the response.
If the HTTP status code is greater than or equal to 400,
it prints an error message.
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        # Display the response body
        print(response.text)
