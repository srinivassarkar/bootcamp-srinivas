<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Updating User Email with SQLAlchemy</title>
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

    <h1>Updating User Email with SQLAlchemy</h1>
    
    <h2>Overview</h2>
    <p>This code demonstrates how to update a user's email address in a SQLite database using SQLAlchemy.</p>
    
    <h2>Key Components</h2>
    <ul>
        <li><strong>Session Creation:</strong> Establishes a session to interact with the database using SQLAlchemy.</li>
        <li><strong>User Update Function:</strong> Defines a function <code>update_user_email</code> that updates the email of a user based on their user ID.</li>
        <li><strong>Commit Changes:</strong> Commits the changes to the database and prints a success message.</li>
        <li><strong>Error Handling:</strong> Prints a message if the user is not found.</li>
    </ul>
    
    <h2>Code Breakdown</h2>
    <pre><code>from sqlalchemy.orm import sessionmaker
from models import User, engine

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Update user email
def update_user_email(user_id: int, new_email: str):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.email = new_email
        session.commit()
        print(f"User  {user_id} email updated to {new_email}!")
    else:
        print("User  not found!")

if __name__ == "__main__":
    update_user_email(1, "john.doe@example.com")</code></pre>
    
    <h2>Approach Simplification</h2>
    <p>The approach can be simplified into the following steps:</p>
    <ol>
        <li>Import necessary modules from SQLAlchemy and the user model.</li>
        <li>Create a session to interact with the database.</li>
        <li>Define the <code>update_user_email</code> function to update a user's email address.</li>
        <li>Query the user by their ID and update the email if the user exists.</li>
        <li>Commit the changes to the database and print a success message or an error message if the user is not found.</li>
    </ol>

    <div class="note">
        <strong>Note:</strong> This content was generated using Blackbox AI.
    </div>

</body>
</html>