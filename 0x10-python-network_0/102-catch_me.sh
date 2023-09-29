#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me causes a server to respond w# msg
curl -sX PUT -H "Origin: HolbertonSchool" -L --max-redirs -1 -d "user_id=98" "0.0.0.0:5000/catch_me"
