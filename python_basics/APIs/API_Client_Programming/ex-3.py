import requests
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