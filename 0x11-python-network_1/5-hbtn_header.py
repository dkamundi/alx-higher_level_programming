#!/usr/bin/python3
"""
Module Description: This script sends a request to a given URL and displays the value of the X-Request-Id variable in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    headers = response.headers

    if 'X-Request-Id' in headers:
        request_id = headers['X-Request-Id']
        print(request_id)

