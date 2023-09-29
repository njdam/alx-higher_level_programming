#!/bin/bash
# A Bash script to take in a URL, sends a POST request to the passed URL
curl -sLX POST -d "email=test%40gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
