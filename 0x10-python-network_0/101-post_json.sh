#!/bin/bash
# A Bash script to send JSON POST request to URL and displays body response
curl -sLX POST -H "Content-Type: application/json" -d "$([ -f "$2" ] && cat "$2" )" "$1"
