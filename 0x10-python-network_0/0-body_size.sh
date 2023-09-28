#!/bin/bash
# A Bash script to take in a URL, sends a request and displays size of body
curl -sI "$1" | grep -oiE "Content-Length: [0-9]+" | cut -d " " -f2
