# FastAPI Static Files Example

<div class="content">

## Problem Approach

This FastAPI application demonstrates how to serve static files from a specified directory. It allows users to access static content such as images, CSS, and JavaScript files.

### Why?

Serving static files is essential for web applications that require assets like stylesheets, scripts, or images. This example shows how to configure FastAPI to serve these files efficiently.

### What?

The application mounts a static file directory ("/static") where users can access static files. It also provides a root endpoint ("/") that returns a simple JSON message.

### How?

The application uses FastAPI's `StaticFiles` middleware to serve files from the "static" directory. When a request is made to the "/static" path, the server responds with the requested static file.

</div>

## Python Code

<pre>from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
    </pre>

<div class="note">**Note:** This code was developed using Blackbox AI, which helps save time and work faster.</div>