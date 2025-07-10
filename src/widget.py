from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data_from_user: str) -> str:
    """Функция, обрабатывающая информацию о картах и счетах"""
    card_type_list = []
    digit_type_list = []
    card_info_list = data_from_user.split()

    for symbol in card_info_list:
        if symbol.isalpha():
            card_type_list.append(symbol)
    card_type = " ".join(card_type_list)

    for symbol in card_info_list:
        if symbol.isdigit():
            digit_type_list.append(symbol)
    digit_type = " ".join(digit_type_list)

    if "счет" in card_type.lower():
        full_info = card_type + " " + get_mask_account(account_number=int(digit_type))
    else:
        full_info = card_type + " " + get_mask_card_number(card_number=int(digit_type))

    return full_info


def get_date(full_date: str) -> str:
    """Функция обработки формата даты"""

    required_date = full_date[8:10] + "." + full_date[5:7] + "." + full_date[:4]
    return required_date
