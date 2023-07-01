#!/bin/bash

# Makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with "You got me!"
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" "http://0.0.0.0:5000/catch_me" -H "Content-Type: application/x-www-form-urlencoded" -H "Referer: http://0.0.0.0:5000/catch_me"
