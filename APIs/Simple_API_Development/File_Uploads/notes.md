# FastAPI File Upload Example

<div class="content">

## Problem Approach

This FastAPI application demonstrates how to upload files to the server. It allows users to send files via HTTP POST requests.

### Why?

File uploads are a common requirement in web applications, enabling users to share documents, images, and other files. This example shows how to handle file uploads using FastAPI.

### What?

The application provides an endpoint ("/upload/") that accepts file uploads and saves them to a specified directory on the server.

### How?

The application uses FastAPI's `UploadFile` and `File` classes to handle file uploads. The uploaded file is read and saved to the "uploads" directory.

</div>

## Python Code

<pre>from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/upload/")
def upload_file(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        buffer.write(file.file.read())
    return {"filename": file.filename}
    </pre>

<div class="note">**Note:** This code was developed using Blackbox AI, which helps save time and work faster.</div>