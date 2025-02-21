<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fetch User Repositories from GitHub</title>
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

    <h1>Fetch User Repositories from GitHub</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This script fetches the repositories of a specified GitHub user using the GitHub GraphQL API. It demonstrates how to authenticate and make GraphQL queries in Python.</p>
        
        <h3>Why?</h3>
        <p>Accessing user repositories programmatically allows developers to analyze, manage, or display repository information in various applications.</p>
        
        <h3>What?</h3>
        <p>The script retrieves the first 10 repositories of a specified user, including their names and descriptions, using a GraphQL query.</p>
        
        <h3>How?</h3>
        <p>Using the <code>gql</code> library, the script sets up a transport layer for the GraphQL API, constructs a query to fetch repository data, and processes the response.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from typing import List, Dict
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the environment variable
github_token = os.getenv('GITHUB_TOKEN')

def fetch_user_repos(token: str, username: str) -> List[Dict]:
    transport = RequestsHTTPTransport(
        url="https://api.github.com/graphql",
        headers={"Authorization": f"Bearer {token}"},
    )
    client = Client(transport=transport)
    query = gql(""" 
        query { 
            user(login: "%s") { 
                repositories(first: 10) { 
                    nodes { 
                        name 
                        description 
                    } 
                } 
            } 
        } 
    """ % username)
    result = client.execute(query)
    return result["user"]["repositories"]["nodes"]

if __name__ == "__main__":
    token = github_token
    username = "srinivassarkar"
    repos = fetch_user_repos(token, username)
    for repo in repos:
        print(f"Name: {repo['name']}, Description: {repo['description']}")
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>