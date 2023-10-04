"""
Модернизация системы вывода
https://new.contest.yandex.ru/41242/problem?id=149944/2022_10_21/NARIFvQojo
Статус: Решено.
"""

used = set()


def modern_print(string):
    if string not in used:
        used.add(string)
        print(string)
    else:
        None


if __name__ == '__main__':
    t1 = modern_print("Hello!")
    t2 = modern_print("Hello!")
    assert t2 is None
    for i in range(4):
        print(modern_print(input()))
