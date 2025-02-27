# Fetch Public Repositories from GitHub

This example demonstrates how to interact with the GitHub API to fetch a list of public repositories and extract their names.

## Code Implementation

```python
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
```

## Explanation

The code defines a function to fetch public repositories from GitHub:

- `fetch_public_repos()`: This function sends a GET request to the GitHub API endpoint to retrieve public repositories.
- `response.raise_for_status()`: This line checks if the request was successful (status code 200) and raises an error for any unsuccessful status codes.
- `repos: List[Dict] = response.json()`: This line parses the JSON response into a list of dictionaries.
- `return [repo["name"] for repo in repos]`: This line extracts the names of the repositories and returns them as a list of strings.

## Approach to the Problem

The approach taken in this example is to demonstrate how to interact with REST APIs and parse JSON responses to extract relevant data.

## Why, What, and How

**Why:** To show how to fetch and display public data from GitHub, which can be useful for various applications.

**What:** This code fetches a list of public repositories from GitHub and prints their names.

**How:** By using the `requests` library to make HTTP requests and handle JSON responses, we can easily interact with web APIs.

> **Note:** This example was created using Blackbox AI.
