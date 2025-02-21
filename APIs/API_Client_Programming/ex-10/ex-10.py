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