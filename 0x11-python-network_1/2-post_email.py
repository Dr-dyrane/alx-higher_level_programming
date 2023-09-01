#!/usr/bin/python3
"""
A Python script that takes in a URL and an email, sends a POST request
to the URL with the email as a parameter, and displays the body of the
response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from command-line arguments
    email = sys.argv[2]  # Get the email from command-line arguments
    value = {"email": email}

    # Prepare the data to be sent in the POST request
    data = urllib.parse.urlencode(value).encode('ascii')

    # Create a request object and specify the data and method
    req = urllib.request.Request(url, data)

    # Perform the request and get the response
    with urllib.request.urlopen(req) as response:
        # Decode and print the response body
        print(response.read().decode('utf-8'))
