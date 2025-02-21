
# Approach:

# How: Use the requests library to call the GitHub API endpoint https://api.github.com/repositories.

# What: Fetch a list of public repositories and extract their names.

# Why: To demonstrate how to interact with REST APIs and parse JSON responses.

# When: When you need to fetch and display public data from GitHub.


import requests
from typing import List, Dict

def fetch_public_repos() -> List[str]:
    url = "https://api.github.com/repositories"
    response = requests.get(url)
    response.raise_for_status()
    repos: List[Dict] = response.json()
    return [repo["name"] for repo in repos]

if __name__ == "__main__":
    repo_names = fetch_public_repos()
    for name in repo_names:
        print(name)
        