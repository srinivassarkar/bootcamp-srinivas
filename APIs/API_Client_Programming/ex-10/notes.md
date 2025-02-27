<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fetch Anime Information from AniList</title>
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

    <h1>Fetch Anime Information from AniList</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This script fetches information about a specified anime title from the AniList GraphQL API. It demonstrates how to construct and execute GraphQL queries in Python.</p>
        
        <h3>Why?</h3>
        <p>Accessing detailed information about anime series is valuable for fans, developers, and researchers interested in anime culture and trends. This script provides a simple way to retrieve such data programmatically.</p>
        
        <h3>What?</h3>
        <p>The script retrieves the English title, description, and status of a specified anime from the AniList API.</p>
        
        <h3>How?</h3>
        <p>Using the <code>gql</code> library, the script sets up a transport layer for the GraphQL API, constructs a query to fetch anime data, and processes the response to extract relevant information.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from typing import Dict

def fetch_anime_info(title: str) -> Dict:
    transport = RequestsHTTPTransport(url="https://graphql.anilist.co")
    client = Client(transport=transport)
    query = gql("""
        query {
            Media(search: "%s", type: ANIME) {
                title {
                    english
                }
                description
                status
            }
        }
    """ % title)
    result = client.execute(query)
    return result["Media"]

if __name__ == "__main__":
    title = "Naruto"
    anime_info = fetch_anime_info(title)
    print(f"Title: {anime_info['title']['english']}")
    print(f"Description: {anime_info['description']}")
    print(f"Status: {anime_info['status']}")
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>