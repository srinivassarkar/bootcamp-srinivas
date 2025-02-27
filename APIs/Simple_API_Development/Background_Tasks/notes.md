# FastAPI Background Tasks Example

## Problem Approach

This FastAPI application demonstrates how to use background tasks to send email notifications without blocking the main thread. It allows for asynchronous processing of tasks.

### Why?

Background tasks are useful for performing operations that do not need to be completed immediately, such as sending emails, processing files, or making external API calls. This improves the responsiveness of the application.

### What?

The application provides an endpoint ("/notify/") that accepts a notification request containing an email and a message. The email is sent in the background, allowing the user to receive an immediate response.

### How?

The application uses FastAPI's `BackgroundTasks` feature to add the email-sending function as a background task. When a request is made to the notify endpoint, the task is scheduled to run after the response is sent.
