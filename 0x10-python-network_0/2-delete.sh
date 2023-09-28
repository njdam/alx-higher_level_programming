#!/bin/bash
# A Bash script to send DELETE request to URL passed as the first argument
curl -sX DELETE "$1"
