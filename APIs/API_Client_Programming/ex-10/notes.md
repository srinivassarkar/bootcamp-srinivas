# Fetch Anime Information from AniList

<div class="content">

## Problem Approach

This script fetches information about a specified anime title from the AniList GraphQL API. It demonstrates how to construct and execute GraphQL queries in Python.

### Why?

Accessing detailed information about anime series is valuable for fans, developers, and researchers interested in anime culture and trends. This script provides a simple way to retrieve such data programmatically.

### What?

The script retrieves the English title, description, and status of a specified anime from the AniList API.

### How?

Using the `gql` library, the script sets up a transport layer for the GraphQL API, constructs a query to fetch anime data, and processes the response to extract relevant information.

