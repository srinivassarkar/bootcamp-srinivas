import requests
from typing import List, Dict

def fetch_best_sellers() -> List[Dict]:
    #url = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=WijMAVAOyKHdD27ubsG7GXZKI7L9DdD5"
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