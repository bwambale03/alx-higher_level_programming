#!/usr/bin/python3

"""
A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your user ID
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    # Get the username and password from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Prepare the authentication for the GitHub API
    auth = HTTPBasicAuth(username, password)

    # Send a GET request to the GitHub API endpoint
    response = requests.get("https://api.github.com/user", auth=auth)

    # Extract the user ID from the API response
    user_data = response.json()
    user_id = user_data.get("id")

    # Print the user ID
    print(user_id)
