<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bluesky API Client</title>
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

    <h1>Bluesky API Client</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This script provides a client for interacting with the Bluesky API, allowing users to authenticate and post messages. It demonstrates the use of environment variables and object-oriented programming in Python.</p>
        
        <h3>Why?</h3>
        <p>Interacting with social media APIs is essential for automating posts and managing content programmatically. This client simplifies the process of posting messages to Bluesky.</p>
        
        <h3>What?</h3>
        <p>The script allows users to log in to their Bluesky account and post messages (skeets) through the API, handling authentication and error management.</p>
        
        <h3>How?</h3>
        <p>Using the <code>atproto</code> library, the script initializes a client with user credentials, authenticates, and posts messages while ensuring proper error handling and input validation.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from atproto import Client
from typing import Optional
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
BLUESKY_HANDLE = os.getenv('BLUESKY_HANDLE')
BLUESKY_APP_PASSWORD = os.getenv('BLUESKY_APP_PASSWORD')

class BlueskyClient:
    def __init__(self, handle: str, app_password: str):
        """
        Initialize the Bluesky API client with user credentials.
        
        :param handle: Bluesky handle (e.g., your-handle.bsky.social)
        :param app_password: App password generated from Bluesky settings
        """
        if not isinstance(handle, str) or not isinstance(app_password, str):
            raise TypeError("Both handle and app password must be strings.")

        self.handle = handle
        self.app_password = app_password
        self.client = Client()

    def login(self) -> bool:
        """Authenticate with the Bluesky API."""
        try:
            self.client.login(self.handle, self.app_password)
            print("Login successful!")
            return True
        except Exception as e:
            print(f"Login failed: {e}")
            return False

    def post_message(self, message: str) -> Optional[dict]:
        """
        Post a message to Bluesky.

        :param message: The content of the post (skeet).
        :return: API response dict if successful, None otherwise.
        """
        if not isinstance(message, str):
            raise TypeError("Message must be a string.")

        if len(message) > 300:  # Bluesky has a character limit
            raise ValueError("Message exceeds the 300-character limit.")

        try:
            response = self.client.send_post(message)
            print("Post successful:", response)
            return response
        except Exception as e:
            print(f"Failed to post message: {e}")
            return None

# Usage
if __name__ == "__main__":
    BLUESKY_HANDLE = "randomtechy.bsky.social"
    BLUESKY_APP_PASSWORD = "xquz-lonh-kalu-tidq"

    bluesky = BlueskyClient(BLUESKY_HANDLE, BLUESKY_APP_PASSWORD)

    if bluesky.login():
        bluesky.post_message("Hello, Bluesky! Posting via API with OOP. #BlueskyAPI")
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed