# FastAPI Basic Authentication Example

<div class="content">

## Problem Approach

This FastAPI application demonstrates basic authentication using HTTP Basic credentials. It shows how to secure a route and validate user credentials.

### Why?

Basic authentication is a simple way to secure API endpoints. It allows you to restrict access to certain routes based on user credentials.

### What?

The application provides a secure route ("/secure") that requires authentication. If the user provides the correct credentials, they receive a welcome message.

### How?

The application uses FastAPI's dependency injection system to handle authentication. It checks the provided username and password against predefined values and raises an HTTP exception if they are incorrect.
## To access route


```
http://localhost:8000/secure
```

 (use admin/password as credentials).