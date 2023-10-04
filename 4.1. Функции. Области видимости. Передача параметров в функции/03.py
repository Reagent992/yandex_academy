"""
Длина числаhttps://new.contest.yandex.ru/41242/problem?id=149944/2022_10_21/6eqEeEVTLJ
Статус: TODO не Решено
"""


def number_length(number: int):
    return len(str(abs(number)))


if __name__ == '__main__':
    assert number_length(12345) == 5
    assert number_length(-100500) == 6
