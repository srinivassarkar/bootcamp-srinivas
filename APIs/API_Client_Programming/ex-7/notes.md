<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fetch Latest SpaceX Launch</title>
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

    <h1>Fetch Latest SpaceX Launch</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This script fetches the latest launch information from SpaceX using the SpaceX GraphQL API. It demonstrates how to make GraphQL queries in Python.</p>
        
        <h3>Why?</h3>
        <p>Accessing real-time launch data is essential for space enthusiasts, developers, and researchers interested in space exploration and technology.</p>
        
        <h3>What?</h3>
        <p>The script retrieves the most recent launch's mission name and rocket name, providing a simple interface to access SpaceX's launch data.</p>
        
        <h3>How?</h3>
        <p>Using the <code>gql</code> library, the script sets up a transport layer for the GraphQL API, constructs a query to fetch the latest launch data, and processes the response.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from typing import Dict

def fetch_latest_launch() -> Dict:
    transport = RequestsHTTPTransport(url="https://api.spacex.land/graphql/")
    client = Client(transport=transport)
    query = gql("""
        query {
            launchesPast(limit: 1) {
                mission_name
                launch_date_local
                rocket {
                    rocket_name
                }
            }
        }
    """)
    result = client.execute(query)
    return result["launchesPast"][0]

if __name__ == "__main__":
    launch = fetch_latest_launch()
    print(f"Mission: {launch['mission_name']}, Rocket: {launch['rocket']['rocket_name']}")
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>