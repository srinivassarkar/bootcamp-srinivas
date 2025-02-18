from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from typing import List, Dict

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
    token = "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"
    username = "srinivassarkar"
    repos = fetch_user_repos(token, username)
    for repo in repos:
        print(f"Name: {repo['name']}, Description: {repo['description']}")

