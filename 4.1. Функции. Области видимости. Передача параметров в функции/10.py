"""
Слияние
https://new.contest.yandex.ru/41242/problem?id=149944/2022_10_21/rbMUpgPUQj
Статус: Решено.
"""


def merge(first: tuple, second: tuple) -> tuple:
    c = []
    i, j = 0, 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            c.append(first[i])
            i += 1
        else:
            c.append(second[j])
            j += 1

    c.extend(first[i:])
    c.extend(second[j:])
    return tuple(c)


if __name__ == '__main__':
    assert merge((1, 2), (3, 4, 5)) == (1, 2, 3, 4, 5)
    assert merge((7, 12), (1, 9, 50)) == (1, 7, 9, 12, 50)
