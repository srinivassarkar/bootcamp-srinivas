import requests
from typing import List, Dict

def fetch_characters() -> List[Dict]:
    url = "https://rickandmortyapi.com/api/character"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["results"]

if __name__ == "__main__":
    characters = fetch_characters()
    for character in characters:
        print(f"Name: {character['name']}, Species: {character['species']}")