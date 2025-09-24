from src.config_logging import *  # Включаем конфигурирование логирования
from src.masks import get_mask_card_number, get_mask_account

if __name__ == "__main__":
    # Тестируем маскировку номера карты
    card_number = 1234567890123456
    masked_card = get_mask_card_number(card_number)
    print(f"Маскированный номер карты: {masked_card}")

    # Тестируем маскировку номера счёта
    account_number = 123456789012
    masked_account = get_mask_account(account_number)
    print(f"Маскированный номер счёта: {masked_account}")
