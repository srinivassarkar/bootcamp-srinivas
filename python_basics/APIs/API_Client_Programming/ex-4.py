import requests
import sys
from typing import Dict

# API_KEY = "0233c7695f99f4daa61475a720a71307"  

def fetch_weather(city: str, api_key: str) -> Dict:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <city>")
        sys.exit(1)

    city = sys.argv[1]
    weather_data = fetch_weather(city, API_KEY)
    print(f"Temperature: {weather_data['main']['temp']}K")
    print(f"Weather: {weather_data['weather'][0]['description']}")
