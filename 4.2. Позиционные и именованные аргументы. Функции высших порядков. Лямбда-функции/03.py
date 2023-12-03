"""
Функциональный нод 2.0
https://new.contest.yandex.ru/41243/problem?id=149944/2022_11_05/LpMdfMRz2k
Status: Solved.
"""


def gcd(*numbers):
    result = 0
    max_numbers = max(numbers)
    for i in range(1, max_numbers + 1):
        t = [digit % i == 0 for digit in numbers]
        if all(t):
            result = i

    return result


if __name__ == "__main__":
    assert gcd(3) == 3
    assert gcd(36, 48, 156, 100500) == 12
