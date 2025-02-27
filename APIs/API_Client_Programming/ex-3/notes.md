# Fetch Public Events from GitHub

<div class="content">

## Problem Approach

This script fetches public events from the GitHub API. It demonstrates how to make a simple HTTP GET request to retrieve data and process it in Python.

### Why?

Understanding how to interact with APIs is crucial for modern software development. GitHub's events API provides insights into various activities happening in repositories.

### What?

The script retrieves a list of public events from GitHub and prints the type of each event along with the repository name.

### How?

Using the `requests` library, the script sends a GET request to the GitHub events endpoint, processes the JSON response, and prints relevant information.

</div>

## Python Code

<pre>import requests
from typing import List, Dict

def fetch_public_events() -> List[Dict]:
    url = "https://api.github.com/events"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    events = fetch_public_events()
    for event in events:
        print(f"Type: {event['type']}, Repo: {event['repo']['name']}")
    </pre>

<div class="note">**Note:** This code was developed using Blackbox AI, which helps save time and work faster.</div>