#!/usr/bin/python3

"""
This script takes a URL as a command-line argument,
sends a request to the URL, and displays the body of the response.

Usage: ./script_name.py <URL>

Example: ./script_name.py http://example.com
"""

import sys
import requests


if __name__ == "__main__":
    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check the status code of the response
    if response.status_code >= 400:
        # If there is an error, display the error code
        print("Error code: {}".format(response.status_code))
    else:
        # If the request is successful, display the response body
        print(response.text)
