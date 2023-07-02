#!/usr/bin/python3

"""
A script that lists the 10 most recent commits on a given GitHub repository.
"""

import sys
import requests


if __name__ == "__main__":
    # Construct the API URL using the provided repository and owner names
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        owner_name, repository_name)

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Parse the JSON response into a list of commits
    commits = response.json()

    try:
        # Loop through the first 10 commits (or fewer if available)
        for commit in commits[:10]:
            # Extract the commit SHA and author name
            commit_sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]

            # Print the commit SHA and author name
            print("{}: {}".format(commit_sha, author_name))
    except IndexError:
        pass
