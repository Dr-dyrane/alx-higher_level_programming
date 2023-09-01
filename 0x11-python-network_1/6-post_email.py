#!/usr/bin/python3
"""
A Python script that sends a POST request to a URL with an email
parameter and displays the body of the response.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email parameter
    data = {'email': email}

    # Send a POST request to the URL with the email parameter
    response = requests.post(url, data=data)

    # Display the response body
    print("Your email is:", response.text)
