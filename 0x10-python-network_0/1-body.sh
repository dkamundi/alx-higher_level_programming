#!/bin/bash
# Script: Get request body
# Sends a GET request to a URL and displays the body of the response

URL=$1

response=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

if [ "$response" -eq 200 ]; then
    curl -s "$URL"
fi

