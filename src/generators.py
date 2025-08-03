def filter_by_currency(transactions, currency_code):
    """Функция принимает на вход список словарей(транзакции) и возвращает
    транзакции с заданной валютой"""
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction


from typing import Generator

def transaction_descriptions(transactions: list) -> Generator[str, None, None]:
    """Генератор, который принимает список словарей с транзакциями
     и возвращает описание каждой операции по очереди"""
    for i in transactions:
        yield i["description"]


def card_number_generator():
    """Генератор, который выдает номера банковских карт
    в формате XXXX XXXX XXXX XXXX"""
