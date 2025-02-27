<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fetch Characters from Rick and Morty API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1 {
            color: #2c3e50;
        }
        pre {
            background-color: #fff;
            border: 1px solid #ccc;
            padding: 10px;
            overflow-x: auto;
        }
        .content {
            margin-bottom: 20px;
        }
        .note {
            background-color: #e7f3fe;
            border-left: 6px solid #2196F3;
            padding: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>Fetch Characters from Rick and Morty API</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This script fetches character data from the Rick and Morty API. It demonstrates how to make HTTP requests and handle JSON responses in Python.</p>
        
        <h3>Why?</h3>
        <p>Accessing character data from popular media franchises like Rick and Morty can be useful for fan applications, data analysis, or simply for fun. This script provides a straightforward way to retrieve such data.</p>
        
        <h3>What?</h3>
        <p>The script retrieves a list of characters from the Rick and Morty API, including their names and species.</p>
        
        <h3>How?</h3>
        <p>Using the <code>requests</code> library, the script sends a GET request to the Rick and Morty API, processes the JSON response, and extracts relevant character information.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
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
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>