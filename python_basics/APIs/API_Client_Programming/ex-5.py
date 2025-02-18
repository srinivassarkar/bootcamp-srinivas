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
