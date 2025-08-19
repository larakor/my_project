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
#print(fin_operation_list("data/operations.json"))
