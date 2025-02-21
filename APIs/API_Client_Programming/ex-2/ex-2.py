# to run : python ex-2.py <github_username>
# to run :  python ex-2.py srinivassarkar


import requests
import sys
from typing import Dict

def fetch_user_details(username: str) -> Dict:
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <username>")
        sys.exit(1)
    username = sys.argv[1]
    user_details = fetch_user_details(username)
    print(f"Name: {user_details.get('name')}")
    print(f"Public Repos: {user_details.get('public_repos')}")