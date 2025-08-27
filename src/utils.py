import json

from src.external_api import convert_currency


def fin_operation_list(data_from_file):
    """Принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях."""
    try:
        with open(data_from_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Проверяем, является ли прочитанный объект списком
        if isinstance(data, list):
            return data
        else:
            print("Ошибка: данные в файле не являются списком.")
            return []

    except FileNotFoundError:
        print(f"Ошибка: файл {data_from_file} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: невозможно декодировать файл {data_from_file}.")
        return []


"""Реализация функций для возврата и конвертации суммы"""


def calculate_transaction_amount(transaction, api_key):
    """Функция для возврата суммы транзакции"""
    amount = float(transaction["amount"])
    currency = transaction.get("currency", "RUB").upper()

    # Конвертация суммы в рубли, если валюта отлична от RUB
    if currency != "RUB":
        converted_amount = convert_currency(amount, currency, "RUB", api_key)
        return round(float(converted_amount), 2)
    else:
        return amount
