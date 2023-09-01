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

    # Get the response content and type
    content = response.text
    content_type = type(content).__name__

    print("Body response:")
    print("    - type:", content_type)
    print("    - content:", content)
