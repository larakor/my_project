import unittest
from unittest.mock import mock_open, patch

from src import external_api  # Импортируем модуль целиком
from src.utils import calculate_transaction_amount, fin_operation_list


class TestFinOperationList(unittest.TestCase):

    # Тест на корректный JSON-файл с данными
    @patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]')
    def test_valid_json_file(self, mock_file):
        result = fin_operation_list('valid_file.json')
        expected_result = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
        self.assertEqual(result, expected_result, "Функция должна вернуть корректный список транзакций")


class TestInputTransaction(unittest.TestCase):

    def test_empty_file(self):
        with patch("builtins.open", mock_open(read_data="")):
            result = fin_operation_list("path/to/mockfile.json")
            self.assertEqual(result, [])

    def test_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            result = fin_operation_list("path/to/mockfile.json")
            self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()


class TestCalculateTransactionAmount(unittest.TestCase):

    class TestCalculateTransactionAmount(unittest.TestCase):

        @patch.object(external_api, "convert_currency")
        def test_calculate_amount_USD_to_RUB(self, mock_convert):
            # Устанавливаем значение для функции convert_currency
            mock_convert.return_value = 750.0
            transaction = {"amount": 10, "currency": "USD"}
            result = calculate_transaction_amount(transaction, "fake_api_key")
            self.assertEqual(result, 750.0)

    @patch("src.external_api.convert_currency")
    def test_same_currency_no_conversion(self, mock_convert):
        transaction = {"amount": 100, "currency": "RUB"}
        result = calculate_transaction_amount(transaction, "fake_api_key")
        self.assertEqual(result, 100)
        mock_convert.assert_not_called()  # Убеждаемся, что конвертация не выполнялась

    @patch("src.external_api.convert_currency")
    def test_empty_transaction(self, mock_convert):
        empty_transaction = {}
        with self.assertRaises(KeyError):
            calculate_transaction_amount(empty_transaction, "fake_api_key")


if __name__ == "__main__":
    unittest.main()
