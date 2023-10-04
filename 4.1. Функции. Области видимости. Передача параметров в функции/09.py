"""
Простая задача 5.0
https://new.contest.yandex.ru/41242/problem?id=149944/2022_10_21/zOVzyYYwkQ
Статус: Решено.
"""


def is_prime(digit: int) -> bool:
    if digit % 2 == 0:
        return digit == 2
    d = 3
    while d * d <= digit and digit % d != 0:
        d += 2
    return d * d > digit


if __name__ == '__main__':
    assert is_prime(1001459) is True
    assert is_prime(79701) is False
