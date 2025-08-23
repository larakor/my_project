import requests


def convert_currency(amount, from_currency, to_currency, api_key):
    """Функция конвертации валюты в рубли"""
    base_url = "https://api.apilayer.com/exchangerates_data/latest"
    headers = {
        "apikey": api_key
    }
    params = {
        "base": from_currency,
        "symbols": to_currency
    }

    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code == 200:
        rates = response.json()["rates"]
        exchange_rate = rates.get(to_currency)
        if exchange_rate:
            return amount * exchange_rate
        else:
            raise ValueError(f"Exchange rate for {to_currency} not found.")
    else:
        raise ConnectionError(f"Failed to fetch exchange rates. Status code: {response.status_code}")