#!/usr/bin/python3
"""
Module Description: This script uses Basic Authentication with a personal access token to access the GitHub API and displays the user id.
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    try:
        print(r.json().get('id'))
    except ValueError:
        print('Not a valid JSON')

