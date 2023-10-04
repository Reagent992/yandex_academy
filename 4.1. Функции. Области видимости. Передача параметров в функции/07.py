"""
Шахматный «обед»
https://new.contest.yandex.ru/41242/problem?id=149944/2022_10_21/aYQJ5HMc7N
Статус: Решено.
"""


def can_eat(start: tuple, finish: tuple) -> bool:
    long = abs(start[0] - finish[0])
    short = abs(start[1] - finish[1])
    if long == 2 and short == 1:
        return True
    elif short == 2 and long == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    assert can_eat((2, 1), (4, 2)) is True
    assert can_eat((5, 5), (6, 6)) is False
    assert can_eat((0, 0), (2, 1)) is True
