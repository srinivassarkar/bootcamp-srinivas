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