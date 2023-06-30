#!/usr/bin/python3
"""
Module Description: This script fetches https://alx-intranet.hbtn.io/status using requests.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    
    try:
        response.raise_for_status()
        data = response.text
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
    except:
        print("HTTP Error occurred:", e)
