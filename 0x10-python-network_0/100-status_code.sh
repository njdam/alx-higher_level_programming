#!/bin/bash
# A Bash script to send a request to a URL passed to display status code
curl -sw "%{response_code}" -o /dev/null "$1"
