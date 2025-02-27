<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Background Tasks Example</title>
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

    <h1>FastAPI Background Tasks Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This FastAPI application demonstrates how to use background tasks to send email notifications without blocking the main thread. It allows for asynchronous processing of tasks.</p>
        
        <h3>Why?</h3>
        <p>Background tasks are useful for performing operations that do not need to be completed immediately, such as sending emails, processing files, or making external API calls. This improves the responsiveness of the application.</p>
        
        <h3>What?</h3>
        <p>The application provides an endpoint ("/notify/") that accepts a notification request containing an email and a message. The email is sent in the background, allowing the user to receive an immediate response.</p>
        
        <h3>How?</h3>
        <p>The application uses FastAPI's <code>BackgroundTasks</code> feature to add the email-sending function as a background task. When a request is made to the notify endpoint, the task is scheduled to run after the response is sent.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the request body
class Notification(BaseModel):
    email: str
    message: str

def send_email_notification(email: str, message: str):
    # Simulate sending an email
    print(f"Sending email to {email}: {message}")

@app.post("/notify/")
def notify(notification: Notification, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email_notification, notification.email, notification.message)
    return {"message": "Notification sent in the background"}
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>