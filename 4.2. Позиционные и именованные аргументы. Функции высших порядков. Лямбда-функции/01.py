"""
Генератор списков
https://new.contest.yandex.ru/41243/problem?id=149944/2022_11_05/PG5RUdm46m
Status: Solved.
"""


def make_list(lenght, value=0):
    return [value] * lenght


if __name__ == "__main__":
    assert make_list(3) == [0, 0, 0]
    assert make_list(5, 1) == [1, 1, 1, 1, 1]
