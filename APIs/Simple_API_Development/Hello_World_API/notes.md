<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Hello World Example</title>
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

    <h1>FastAPI Hello World Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This FastAPI application demonstrates a simple API that returns a "Hello, World!" message when accessed.</p>
        
        <h3>Why?</h3>
        <p>This example serves as a basic introduction to FastAPI, showcasing how to create a simple web application with minimal code.</p>
        
        <h3>What?</h3>
        <p>The application provides a root endpoint ("/") that returns a JSON response containing a greeting message.</p>
        
        <h3>How?</h3>
        <p>The application uses FastAPI's routing capabilities to define an endpoint and return a JSON response when the root URL is accessed.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>