<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fetch Top Posts from Hacker News</title>
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

    <h1>Fetch Top Posts from Hacker News</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This script fetches the top posts from Hacker News using the Hacker News API. It demonstrates how to make HTTP requests and handle JSON responses in Python.</p>
        
        <h3>Why?</h3>
        <p>Accessing the latest stories from Hacker News is useful for developers, tech enthusiasts, and anyone interested in current technology trends and discussions.</p>
        
        <h3>What?</h3>
        <p>The script retrieves the top 10 stories from Hacker News, including their titles and URLs.</p>
        
        <h3>How?</h3>
        <p>Using the <code>requests</code> library, the script sends GET requests to the Hacker News API to fetch the top story IDs and then retrieves detailed information for each story.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
import requests
from typing import List, Dict

def fetch_top_posts() -> List[Dict]:
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    story_ids = requests.get(top_stories_url).json()
    posts = []
    for story_id in story_ids[:10]:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story = requests.get(story_url).json()
        posts.append({"title": story["title"], "url": story.get("url", "No URL")})
    return posts

if __name__ == "__main__":
    posts = fetch_top_posts()
    for post in posts:
        print(f"Title: {post['title']}, URL: {post['url']}")
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>