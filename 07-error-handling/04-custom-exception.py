class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)


def divide(a, b):
    if b == 0:
        raise MyCustomException("Division by zero is not allowed")
    return a / b


try:
    result = divide(10, 0)
except MyCustomException as e:
    print("An error occurred:", e)
else:
    print("Result:", result)
