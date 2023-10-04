"""
Функциональный НОД
https://new.contest.yandex.ru/41242/problem?id=149944/2022_10_21/RYegF3IecG
Статус: Решено.
"""


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    assert gcd(12, 45) == 3
    assert gcd(144, 96) == 48
