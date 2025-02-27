<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Item Creation Example</title>
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

    <h1>FastAPI Item Creation Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This FastAPI application demonstrates how to create an item using a POST request. It utilizes Pydantic for data validation and serialization.</p>
        
        <h3>Why?</h3>
        <p>Creating and validating data is a common requirement in web applications. This example shows how to handle data input effectively using FastAPI and Pydantic.</p>
        
        <h3>What?</h3>
        <p>The application provides an endpoint ("/items/") that accepts a JSON payload to create a new item, which includes a name and an optional description.</p>
        
        <h3>How?</h3>
        <p>The application defines a Pydantic model to validate the incoming data. When a POST request is made to the endpoint, the data is validated and returned in the response.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None

@app.post("/items/")
def create_item(item: Item):
    return item
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>