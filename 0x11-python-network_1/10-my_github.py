#!/usr/bin/python3
"""
Module Description: This script uses Basic Authentication with a personal access token to access the GitHub API and displays the user id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    auth = (username, password)
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        data = response.json()
        user_id = data['data']['id']

        print("User ID:", user_id)
    else:
        print("Error accessing GitHub API:", response.status_code)

