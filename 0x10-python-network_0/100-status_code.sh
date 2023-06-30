#!/bin/bash
# Bash script to send a request to a URL and display only the status code

if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url=$1

status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")

echo "Status code: $status_code"

