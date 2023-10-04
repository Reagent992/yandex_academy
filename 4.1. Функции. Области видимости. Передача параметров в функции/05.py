"""
Числовая строка
https://new.contest.yandex.ru/41242/problem?id=149944/2022_10_21/q5x4e7gb7c
Статус: Решено.
"""


def split_numbers(string_of_numbers: str) -> tuple:
    return tuple(map(int, string_of_numbers.split()))


if __name__ == '__main__':
    assert split_numbers('1 2 3 4 5') == (1, 2, 3, 4, 5)
    assert split_numbers("1 -2 3 -4 5") == (1, -2, 3, -4, 5)
