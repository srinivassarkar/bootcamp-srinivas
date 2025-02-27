# Currency Converter

<div class="content">

## Problem Approach

This script converts a specified amount of money from USD to a target currency using the ExchangeRate API. It demonstrates how to make HTTP requests and handle JSON responses in Python.

### Why?

Currency conversion is a common requirement in financial applications, e-commerce platforms, and travel-related services. This script provides a simple way to perform such conversions programmatically.

### What?

The script retrieves the latest exchange rates for USD and converts a specified amount to the target currency.

### How?

Using the `requests` library, the script sends a GET request to the ExchangeRate API, processes the JSON response to extract the exchange rates, and calculates the converted amount.
