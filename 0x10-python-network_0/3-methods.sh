#!/bin/bash
# Script: 3-methods.sh
# Displays all HTTP methods the server will accept for a given URL

URL=$1

response=$(curl -sI -X OPTIONS "$URL" | grep "Allow:" | sed 's/Allow: //')

echo "$response"

