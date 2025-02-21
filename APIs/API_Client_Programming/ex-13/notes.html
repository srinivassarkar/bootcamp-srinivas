<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fetch GitHub Contributions</title>
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

    <h1>Fetch GitHub Contributions</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This script fetches the number of contributions made by a specified GitHub user over the last year. It demonstrates how to scrape web data using Python.</p>
        
        <h3>Why?</h3>
        <p>Tracking contributions on GitHub is important for developers to showcase their activity and engagement in open-source projects. This script provides a way to programmatically retrieve that information.</p>
        
        <h3>What?</h3>
        <p>The script retrieves the total number of contributions made by a specified user in the last year by scraping their GitHub contributions page.</p>
        
        <h3>How?</h3>
        <p>Using the <code>requests</code> library, the script sends a GET request to the GitHub contributions page, and with the help of <code>BeautifulSoup</code>, it parses the HTML to extract the total contributions.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
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
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>