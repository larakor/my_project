import json
from src.external_api import convert_currency
import logging

# Получаем объект логера для модуля utils
logger = logging.getLogger('utils')


def fin_operation_list(data_from_file):
    """Принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях."""
    try:
        logger.info(f"Попытка чтения файла {data_from_file}")  # Добавление логирования
        with open(data_from_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Проверяем, является ли прочитанный объект списком
        if isinstance(data, list):
            logger.info(f"Успешно считаны данные из файла {data_from_file}: количество транзакций - {len(data)}")
            return data
        else:
            logger.error(f"Ошибка: данные в файле {data_from_file} не являются списком.")  # Добавление логирования
            return []

    except FileNotFoundError:
        logger.error(f"Ошибка: файл {data_from_file} не найден.")  # Добавление логирования
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка: невозможно декодировать файл {data_from_file}.")  # Добавление логирования
        return []


"""Реализация функций для возврата и конвертации суммы"""


def calculate_transaction_amount(transaction, api_key):
    """Функция для возврата суммы транзакции"""
    amount = float(transaction["amount"])
    currency = transaction.get("currency", "RUB").upper()

    # Логируем факт начала расчета суммы
    logger.info(f"Расчет суммы транзакции: сумма={amount}, валюта={currency}")

    # Конвертация суммы в рубли, если валюта отлична от RUB
    if currency != "RUB":
        converted_amount = convert_currency(amount, currency, "RUB", api_key)
        final_amount = round(float(converted_amount), 2)
        logger.info(f"Сумма конвертирована: оригинал={amount}{currency}, итог={final_amount}RUB")
        return final_amount
    else:
        logger.info(f"Транзакция в рублях: сумма={amount}RUB")  # Добавление логирования
        return amount
