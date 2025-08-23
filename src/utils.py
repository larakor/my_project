import json


def fin_operation_list(data_from_file):
    """Принимает на вход путь до JSON-файла и возвращает список словарей
     с данными о финансовых транзакциях. """
    try:
        with open(data_from_file, "r", encoding="utf-8") as f:
            transactions = json.load(f)

            # Проверяем, является ли прочитанная структура списком
            if isinstance(transactions, list):
                return transactions
            else:
                return []
    except (json.JSONDecodeError, FileNotFoundError, TypeError):
        return []

#Реализация функций для возврата и конвертации суммы
import requests
from dotenv import load_dotenv
import os
from decimal import Decimal
from external_api import convert_currency

# Загрузка переменных окружения из .env
load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")

def calculate_transaction_amount(transaction):
    """Функция для возврата суммы транзакции"""
    amount = float(transaction["amount"])
    currency = transaction.get("currency", "RUB").upper()

    # Конвертация суммы в рубли, если валюта отлична от RUB
    if currency != "RUB":
        converted_amount = convert_currency(amount, currency, "RUB", API_KEY)
        return round(float(converted_amount), 2)
    else:
        return amount
