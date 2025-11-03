from unittest import TestCase, mock
from src.csv_xlsx_reader import read_transactions_from_csv, read_transactions_from_excel


class TestTransactionReader(TestCase):

    @mock.patch("pandas.read_csv")
    def test_read_transactions_from_csv(self, mock_read_csv):
        # Подготавливаем моковские данные
        mock_data = [
            {'id': 1, 'state': 'EXECUTED', 'amount': 100},
            {'id': 2, 'state': 'CANCELED', 'amount': 200}
        ]
        mock_read_csv.return_value = mock.Mock(to_dict=lambda x: mock_data if x == 'records' else None)

        # Проверяем чтение из CSV
        result = read_transactions_from_csv('path/to/file.csv')
        self.assertEqual(result, mock_data)
        mock_read_csv.assert_called_once_with('path/to/file.csv')

    @mock.patch("pandas.read_excel")
    def test_read_transactions_from_excel(self, mock_read_excel):
        # Подготавливаем моковские данные
        mock_data = [
            {'id': 1, 'state': 'EXECUTED', 'amount': 100},
            {'id': 2, 'state': 'CANCELED', 'amount': 200}
        ]
        mock_read_excel.return_value = mock.Mock(to_dict=lambda x: mock_data if x == 'records' else None)

        # Проверяем чтение из Excel
        result = read_transactions_from_excel('path/to/file.xlsx')
        self.assertEqual(result, mock_data)
        mock_read_excel.assert_called_once_with('path/to/file.xlsx')
