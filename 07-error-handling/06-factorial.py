class InvalidArgument(Exception):
    def __init__(self, message):
        super().__init__(message)


def fact(n: int):  # fact(5) -> 5 * 4 * 3 * 2 * 1 = 120
    if not isinstance(n, int):
        raise InvalidArgument("The argument should be int")
    if n < 0:
        raise InvalidArgument("The argument should be positive")

    if n == 0:
        return 1
    return n * fact(n-1)


print(fact("a"))
