#!/usr/bin/python3

"""
This script takes a URL and an email address as command-line arguments,
sends a POST request to the URL with the email as a parameter, and displays
the body of the response.

Usage: ./6-post_email.py <URL> <email>

Example: ./6-post_email.py http://0.0.0.0:5000/post_email
hr@holbertonschool.com
"""

import requests
import sys
from flask import Flask


app = Flask(__name__)


def post_email(url, email):

    """Sends a POST request to the specified URL with the
    email as a parameter."""
    data = {'email': email}
    response = requests.post(url, data=data)
    print("Your email is: ", email)
    print(response.text)


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
    app.run(host='0.0.0.0', port=5000)
