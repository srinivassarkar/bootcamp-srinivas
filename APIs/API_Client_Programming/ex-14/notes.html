<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fetch Best Sellers from NY Times API</title>
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
        .book {
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
            background-color: #fff;
        }
        .book img {
            max-width: 100px;
            margin-right: 10px;
        }
    </style>
</head>
<body>

    <h1>Fetch Best Sellers from NY Times API</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This script fetches the current best-selling hardcover fiction books from the New York Times API. It demonstrates how to make HTTP requests and handle JSON responses in Python.</p>
        
        <h3>Why?</h3>
        <p>Accessing best-selling book data is valuable for readers, authors, and publishers to understand market trends and popular literature.</p>
        
        <h3>What?</h3>
        <p>The script retrieves a list of best-selling hardcover fiction books, including their titles, authors, descriptions, publishers, and links to purchase them on Amazon.</p>
        
        <h3>How?</h3>
        <p>Using the <code>requests</code> library, the script sends a GET request to the NY Times API, processes the JSON response, and extracts relevant book information.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
import requests
from typing import List, Dict
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the environment variable
nytimes_api_key = os.getenv('NYTIMES_API_KEY')

def fetch_best_sellers() -> List[Dict]:
    url = f"https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key={nytimes_api_key}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return []
    
    data = response.json()
    
    if "results" in data and "books" in data["results"]:
        books = []
        for item in data["results"]["books"]:
            books.append({
                "title": item["title"],
                "author": item["author"],
                "description": item["description"],
                "publisher": item["publisher"],
                "book_image": item["book_image"],
                "amazon_url": item["amazon_product_url"]
            })
        return books
    else:
        print("No results found in the response.")
        return []

if __name__ == "__main__":
    books = fetch_best_sellers()
    if books:
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, Publisher: {book['publisher']}, Description: {book['description']}")
            print(f"Image: {book['book_image']}")
            print(f"Buy here: {book['amazon_url']}\n")
    else:
        print("No books found.")
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>