from functools import wraps


def log(filename=None):
    """Декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            message = f"Запущен вызов функции '{func.__name__}'\n"

            try:
                result = func(*args, **kwargs)
                message += f"Функция '{func.__name__}' выполнена успешно. Результат: {result}\n"
                output = message
            except Exception as err:
                error_message = (
                    f"Вызов функции '{func.__name__}' завершился ошибкой типа {type(err).__name__}. "
                    f"Ошибка произошла с параметрами args={args}, kwargs={kwargs}: {err}\n"
                )
                output = error_message
                raise
            finally:
                if filename is not None:
                    with open(filename, "a") as file:
                        file.write(output)
                else:
                    print(output)

        return wrapper

    return decorator
