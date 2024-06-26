#!/usr/bin/python3
"""
Script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        data = urllib.parse.urlencode({"email": sys.argv[2]})
        data = data.encode("ascii")

        with urllib.request.urlopen(sys.argv[1], data) as response:
            print(response.read().decode("utf-8"))
    else:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
