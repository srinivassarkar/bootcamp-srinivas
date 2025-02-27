<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI File Upload Example</title>
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

    <h1>FastAPI File Upload Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This FastAPI application demonstrates how to upload files to the server. It allows users to send files via HTTP POST requests.</p>
        
        <h3>Why?</h3>
        <p>File uploads are a common requirement in web applications, enabling users to share documents, images, and other files. This example shows how to handle file uploads using FastAPI.</p>
        
        <h3>What?</h3>
        <p>The application provides an endpoint ("/upload/") that accepts file uploads and saves them to a specified directory on the server.</p>
        
        <h3>How?</h3>
        <p>The application uses FastAPI's <code>UploadFile</code> and <code>File</code> classes to handle file uploads. The uploaded file is read and saved to the "uploads" directory.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/upload/")
def upload_file(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        buffer.write(file.file.read())
    return {"filename": file.filename}
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>