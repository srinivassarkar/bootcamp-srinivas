<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Example</title>
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
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background: #fff;
            margin: 5px 0;
            padding: 10px;
            border: 1px solid #ccc;
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

    <h1>FastAPI Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This FastAPI application serves a simple HTML page that displays a list of items. It demonstrates how to use FastAPI with Jinja2 templates to render dynamic content.</p>
        
        <h3>Why?</h3>
        <p>FastAPI is a modern web framework for building APIs with Python. Using templates allows for dynamic content generation, making it easier to create interactive web applications.</p>
        
        <h3>What?</h3>
        <p>The application serves a root endpoint ("/") that returns an HTML page with a list of items.</p>
        
        <h3>How?</h3>
        <p>The application uses FastAPI to define the web server and Jinja2 for rendering HTML templates. When a user accesses the root URL, the server responds with an HTML page that includes the list of items.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    items: List[str] = ["Item 1", "Item 2", "Item 3"]
    return templates.TemplateResponse("index.html", {"request": request, "items": items})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    </pre>

    <h2>HTML Template (index.html)</h2>
    <pre>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Items List</title>
</head>
<body>
    <h1>Items</h1>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
</body>
</html>
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>