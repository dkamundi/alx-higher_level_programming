#!/usr/bin/python3
"""
Module Description: This script sends a request to a given URL and displays the response body, handling HTTP errors.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)

