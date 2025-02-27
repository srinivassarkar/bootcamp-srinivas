<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currency Converter</title>
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

    <h1>Currency Converter</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This script converts a specified amount of money from USD to a target currency using the ExchangeRate API. It demonstrates how to make HTTP requests and handle JSON responses in Python.</p>
        
        <h3>Why?</h3>
        <p>Currency conversion is a common requirement in financial applications, e-commerce platforms, and travel-related services. This script provides a simple way to perform such conversions programmatically.</p>
        
        <h3>What?</h3>
        <p>The script retrieves the latest exchange rates for USD and converts a specified amount to the target currency.</p>
        
        <h3>How?</h3>
        <p>Using the <code>requests</code> library, the script sends a GET request to the ExchangeRate API, processes the JSON response to extract the exchange rates, and calculates the converted amount.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
import requests
from typing import Dict

def convert_currency(amount: float, target_currency: str) -> float:
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    response.raise_for_status()
    rates: Dict = response.json()["rates"]
    return amount * rates[target_currency]

if __name__ == "__main__":
    amount = 100.0
    target_currency = "EUR"
    converted_amount = convert_currency(amount, target_currency)
    print(f"{amount} USD = {converted_amount} {target_currency}")
    </pre>

    <div class="note">
        <strong>Note:</strong> This code was developed using Blackbox AI, which helps save time and work faster.
    </div>

</body>
</html>