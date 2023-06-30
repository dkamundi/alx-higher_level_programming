#!/usr/bin/python3
"""
Module Description: This script sends a POST request to a given URL with an email as a parameter and displays the response body.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)

