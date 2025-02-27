# Fetch User Repositories from GitHub

<div class="content">

## Problem Approach

This script fetches the repositories of a specified GitHub user using the GitHub GraphQL API. It demonstrates how to authenticate and make GraphQL queries in Python.

### Why?

Accessing user repositories programmatically allows developers to analyze, manage, or display repository information in various applications.

### What?

The script retrieves the first 10 repositories of a specified user, including their names and descriptions, using a GraphQL query.

### How?

Using the `gql` library, the script sets up a transport layer for the GraphQL API, constructs a query to fetch repository data, and processes the response.
