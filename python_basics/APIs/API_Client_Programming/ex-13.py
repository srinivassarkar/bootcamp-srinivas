import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def get_contributions(username):
    # GitHub contributions page URL
    url = f"https://github.com/users/{username}/contributions"
    
    # Calculate the start and end dates for the last year
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    
    # Format dates as needed by the URL
    to_date = end_date.strftime('%Y-%m-%d')
    from_date = start_date.strftime('%Y-%m-%d')
    
    # Construct URL with date range
    url_with_dates = f"{url}?from={from_date}&to={to_date}"
    
    try:
        response = requests.get(url_with_dates)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the element that contains the total contributions for the year
        total_contributions_element = soup.find('h2', class_='f4 text-normal mb-2')
        
        if total_contributions_element:
            # Extract the number of contributions
            contributions_text = total_contributions_element.text.split()[0]
            # Remove commas from the number to convert it to an integer
            contributions = int(contributions_text.replace(',', ''))
            return contributions
        else:
            return 0  # If no contributions found or element not present
    
    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <GitHub_username>")
    else:
        username = sys.argv[1]
        contributions = get_contributions(username)
        if contributions is not None:
            print(f"{username} had {contributions} contributions in the last year.")
        else:
            print(f"Could not fetch contributions for {username}.")