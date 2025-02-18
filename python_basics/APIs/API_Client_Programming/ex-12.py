import requests
from typing import List, Dict

def fetch_pokemon_types(pokemon_name: str) -> List[str]:
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    response.raise_for_status()
    pokemon_data: Dict = response.json()
    return [t["type"]["name"] for t in pokemon_data["types"]]

if __name__ == "__main__":
    pokemon_name = "pikachu"
    types = fetch_pokemon_types(pokemon_name)
    print(f"Types: {', '.join(types)}")