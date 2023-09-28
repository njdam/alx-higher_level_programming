#!/bin/bash
# A Bash scriptnto take in URL and displays all HTTP methods
curl -sikLX OPTIONS "$1" | grep -oiE "Allow: .+" | cut -d " " -f2-
