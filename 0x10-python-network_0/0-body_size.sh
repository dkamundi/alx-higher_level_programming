#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes

url=$1
response=$(curl -s -w "%{size_download}" -o /dev/null "$url")
echo "Response Size: $response bytes"
