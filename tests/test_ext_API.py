import unittest
from unittest.mock import Mock, patch

from src.external_api import convert_currency


class TestConvertCurrency(unittest.TestCase):

    @patch("requests.get")
    def test_server_unreachable(self, mock_get):
        # Эмуляция ситуации, когда сервер недоступен
        mock_get.side_effect = ConnectionError("Server unreachable")

        # Проверяем, что функция бросает ошибку ConnectionError
        with self.assertRaises(ConnectionError):
            convert_currency(10, "USD", "RUB", "any_api_key")

    @patch("requests.get")
    def test_successful_conversion(self, mock_get):
        # Создаем моковый объект для имитации ответа API
        mock_response = Mock()
        mock_response.json.return_value = {"rates": {"RUB": 75}}
        mock_response.status_code = 200  # ВАЖНО: задать статус-код 200
        mock_get.return_value = mock_response

        # Выполняем конвертацию
        result = convert_currency(10, "USD", "RUB", "any_api_key")

        # Проверяем результат
        self.assertAlmostEqual(result, 750, delta=0.01)  # 10 долларов * 75 рублей/доллар


if __name__ == "__main__":
    unittest.main()
