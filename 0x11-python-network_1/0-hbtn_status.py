#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
and displays information about the response using urllib.
"""

import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as response:
        content = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
