#!/usr/bin/python3
"""
Module Description: This script sends a request to a given URL and displays the body of the response. It also handles HTTP error codes.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)

