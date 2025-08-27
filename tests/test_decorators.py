import pytest

from src.decorators import log


@log(filename=None)
def my_function(x, y):
    """Тестовая функция с декоратором"""
    return x / y


def test_decorator_log():
    """Тестирование декоратора без выхода ошибки"""

    @log(filename=None)
    def my_function(x, y):
        return x / y


def test_decorator_log_error():
    """Тестирование декоратора с выходом ошибки"""
    with pytest.raises(Exception):
        my_function(6, 0)


def test_decorator_capsys_err(capsys):
    """Тестирование декоратора с выходом ошибки с фикстурой capsys"""
    with pytest.raises(Exception):
        my_function(6, 0)
        captured = capsys.readouterr()
        assert "error" in captured.out


def test_decorator_capsys(capsys):
    """Тестирование декоратора с успешным выходом с фикстурой capsys"""
    my_function(6, 3)
    captured = capsys.readouterr()
    assert (
        "Запущен вызов функции 'my_function'\nФункция 'my_function' выполнена успешно. " "Результат: 2.0\n\n"
    ) in captured.out
