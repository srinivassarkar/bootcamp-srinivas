# Fetch GitHub Contributions

<div class="content">

## Problem Approach

This script fetches the number of contributions made by a specified GitHub user over the last year. It demonstrates how to scrape web data using Python.

### Why?

Tracking contributions on GitHub is important for developers to showcase their activity and engagement in open-source projects. This script provides a way to programmatically retrieve that information.

### What?

The script retrieves the total number of contributions made by a specified user in the last year by scraping their GitHub contributions page.

### How?

Using the `requests` library, the script sends a GET request to the GitHub contributions page, and with the help of `BeautifulSoup`, it parses the HTML to extract the total contributions.
