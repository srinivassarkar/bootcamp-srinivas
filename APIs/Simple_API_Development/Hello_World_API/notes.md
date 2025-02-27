# FastAPI Hello World Example

<div class="content">

## Problem Approach

This FastAPI application demonstrates a simple API that returns a "Hello, World!" message when accessed.

### Why?

This example serves as a basic introduction to FastAPI, showcasing how to create a simple web application with minimal code.

### What?

The application provides a root endpoint ("/") that returns a JSON response containing a greeting message.

### How?

The application uses FastAPI's routing capabilities to define an endpoint and return a JSON response when the root URL is accessed.

</div>

## Python Code

<pre>from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
    </pre>

<div class="note">**Note:** This code was developed using Blackbox AI, which helps save time and work faster.</div>