#!/usr/bin/python3

"""
A script that:
- takes in a letter as a command-line argument
- sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter
- displays the response from the server
"""

import sys
import requests


if __name__ == "__main__":
    # Get the letter from the command-line argument
    letter = "" if len(sys.argv) < 2 else sys.argv[1]

    # Prepare the request payload with the letter as a parameter
    payload = {"q": letter}

    # Send a POST request to the specified URL with the payload
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Try to parse the response as JSON
        json_response = response.json()

        if json_response:
            # If the JSON response is not empty, display the id and name
            print("[{}] {}".format(json_response["id"], json_response["name"]))
        else:
            # If the JSON response is empty, display "No result"
            print("No result")
    except ValueError:
        # If the response is not a valid JSON, display "Not a valid JSON"
        print("Not a valid JSON")
