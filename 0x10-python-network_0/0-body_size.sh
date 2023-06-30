#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes

<<<<<<< HEAD
url=$1
response=$(curl -s -w "%{size_download}" -o /dev/null "$url")
echo "Response Size: $response bytes"
=======
curl -sI "$1" | grep "Content-Length:"| cut -d":" -f2-
>>>>>>> origin/master
