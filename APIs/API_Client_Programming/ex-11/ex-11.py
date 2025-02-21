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