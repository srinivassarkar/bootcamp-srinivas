<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Basic Authentication Example</title>
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

    <h1>FastAPI Basic Authentication Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This FastAPI application demonstrates basic authentication using HTTP Basic credentials. It shows how to secure a route and validate user credentials.</p>
        
        <h3>Why?</h3>
        <p>Basic authentication is a simple way to secure API endpoints. It allows you to restrict access to certain routes based on user credentials.</p>
        
        <h3>What?</h3>
        <p>The application provides a secure route ("/secure") that requires authentication. If the user provides the correct credentials, they receive a welcome message.</p>
        
        <h3>How?</h3>
        <p>The application uses FastAPI's dependency injection system to handle authentication. It checks the provided username and password against predefined values and raises an HTTP exception if they are incorrect.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated

app = FastAPI()
security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "password"
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.get("/secure")
def secure_route(username: Annotated[str, Depends(authenticate)]):
    return {"message": f"Hello, {username}! You are authenticated."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>