#!/usr/bin/python3
import sys
import requests
url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data=data)
print('your email is : ', email)
print(response.text)
