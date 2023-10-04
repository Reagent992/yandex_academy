"""
А роза упала на лапу Азора 7.0
https://new.contest.yandex.ru/41242/problem?id=149944/2022_10_21/4GGEwO93c3
Статус: Решено.
"""


def is_palindrome(digit) -> bool:
    if isinstance(digit, (int, str)):
        digit = list(str(digit))
    return True if digit == digit[::-1] else False


if __name__ == '__main__':
    assert is_palindrome(123) is False
    assert is_palindrome([1, 2, 1, 2, 1]) is True
