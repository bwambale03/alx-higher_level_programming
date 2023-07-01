#!/usr/bin/python3
"""
This is a script that:
- takes a URL and an email address as inputs
- sends a message to the given URL with the email address
- shows the response message received.
"""

import sys
import requests

if __name__ == "__main__":
    # Get the URL from the user
    url = sys.argv[1]

    # Get the email address from the user
    email = sys.argv[2]

    # Prepare the message to send
    message = {"email": email}

    # Send the message to the URL
    response = requests.post(url, data=message)

    # Print the response message received
    print(response.text)
