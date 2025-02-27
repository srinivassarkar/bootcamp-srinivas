<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fetching User with Posts using SQLAlchemy and Pydantic</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        pre {
            background-color: #eaeaea;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: 'Courier New', Courier, monospace;
            color: #d14;
        }
        .note {
            background-color: #fff3cd;
            border-left: 6px solid #ffeeba;
            padding: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>Fetching User with Posts using SQLAlchemy and Pydantic</h1>
    
    <h2>Overview</h2>
    <p>This code demonstrates how to fetch a user along with their posts from a SQLite database using SQLAlchemy and serialize the data using Pydantic.</p>
    
    <h2>Key Components</h2>
    <ul>
        <li><strong>Pydantic Schemas:</strong> Defines schemas for <code>Post</code> and <code>UserWithPosts</code> to validate and serialize data.</li>
        <li><strong>Session Creation:</strong> Establishes a session to interact with the database using SQLAlchemy.</li>
        <li><strong>User Fetching Function:</strong> Defines a function <code>fetch_user_with_posts</code> that retrieves a user and their posts based on user ID.</li>
        <li><strong>Pydantic Serialization:</strong> Uses Pydantic's <code>UserWithPostsSchema</code> to serialize the user data into JSON format.</li>
        <li><strong>Output:</strong> Prints the serialized user data to the console or a message if the user is not found.</li>
    </ul>
    
    <h2>Code Breakdown</h2>
    <pre><code>from sqlalchemy.orm import sessionmaker
from models_with_posts import User, Post, engine
from pydantic import BaseModel

# Pydantic schemas
class PostSchema(BaseModel):
    title: str
    content: str

    class Config:
        from_attributes = True

class UserWithPostsSchema(BaseModel):
    name: str
    email: str
    posts: list[PostSchema]

    class Config:
        from_attributes = True

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Fetch user with posts
def fetch_user_with_posts(user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        return UserWithPostsSchema.from_orm(user)
    return None

if __name__ == "__main__":
    user = fetch_user_with_posts(1)
    if user:
        print(user.json())
    else:
        print("User  not found!")</code></pre>
    
    <h2>Approach Simplification</h2>
    <p>The approach can be simplified into the following steps:</p>
    <ol>
        <li>Import necessary modules from SQLAlchemy and Pydantic.</li>
        <li>Define Pydantic schemas for <code>Post</code> and <code>UserWithPosts</code> to validate and serialize data.</li>
        <li>Create a session to interact with the database.</li>
        <li>Define the <code>fetch_user_with_posts</code> function to retrieve a user and their posts by user ID.</li>
        <li>Use Pydantic's <code>UserWithPostsSchema</code> to serialize the user data into JSON format.</li>
        <li>Print the serialized user data to the console or a message if the user is not found.</li>
    </ol>

    <div class="note">
        <strong>Note:</strong> This content was generated using Blackbox AI.
    </div>

</body>
</html>