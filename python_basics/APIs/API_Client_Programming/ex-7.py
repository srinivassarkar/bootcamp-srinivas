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
    
    
