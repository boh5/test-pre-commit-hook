import secrets
from collections.abc import Iterable


def sum_even_numbers(numbers: Iterable[int]) -> int:
    """
    Given an iterable of integers,
    return the sum of all even numbers in the iterable.
    """
    return sum(num for num in numbers if num % 2 == 0)


def token():
    print(secrets.token_urlsafe())


if __name__ == "__main__":
    token()
