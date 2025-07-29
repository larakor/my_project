import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('value, expected', [
    ('1234567890123456789', 'Некорректный ввод')
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize('value, expected', [
    ('123', 'Некорректный ввод')
    ])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
