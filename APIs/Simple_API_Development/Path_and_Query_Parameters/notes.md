# FastAPI Query Parameter Example

<div class="content">

## Problem Approach

This FastAPI application demonstrates how to create an endpoint that retrieves an item by its ID, with an optional query parameter for additional filtering or searching.

### Why?

Query parameters are commonly used in APIs to provide additional context or filtering options for requests. This example shows how to implement them in FastAPI.

### What?

The application provides an endpoint ("/items/{item_id}") that accepts an item ID as a path parameter and an optional query parameter (q) for additional information.

### How?

The application uses FastAPI's routing capabilities to define an endpoint and the `Query` class to handle optional query parameters with validation (e.g., maximum length).

</div>

## Python Code

<pre>from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = Query(None, max_length=50)):
    return {"item_id": item_id, "q": q}
    </pre>

<div class="note">**Note:** This code was developed using Blackbox AI, which helps save time and work faster.</div>