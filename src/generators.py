from typing import Generator


def filter_by_currency(transactions, currency_code):
    """Функция принимает на вход список словарей(транзакции) и возвращает
    транзакции с заданной валютой"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: list) -> Generator[str, None, None]:
    """Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    for i in transactions:
        yield i["description"]


def card_number_generator(start, stop) -> Generator[str, None, None]:
    """Генератор, который выдает номера банковских карт
    в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, stop):
        card_number = str(number).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
