# FastAPI Example

## Problem Approach

This FastAPI application serves a simple HTML page that displays a list of items. It demonstrates how to use FastAPI with Jinja2 templates to render dynamic content.

### Why?

FastAPI is a modern web framework for building APIs with Python. Using templates allows for dynamic content generation, making it easier to create interactive web applications.

### What?

The application serves a root endpoint ("/") that returns an HTML page with a list of items.

### How?

The application uses FastAPI to define the web server and Jinja2 for rendering HTML templates. When a user accesses the root URL, the server responds with an HTML page that includes the list of items.

### installation

```
pip install fastapi uvicorn jinja2
```

### To Run

```
uvicorn main:app --reload
```