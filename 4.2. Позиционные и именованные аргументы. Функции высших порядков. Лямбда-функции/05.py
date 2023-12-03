"""
Подготовка данных
https://new.contest.yandex.ru/41243/problem?id=149944/2022_11_05/iXPqBtv90d
Status: Solved.
"""


def to_string(*items, sep=' ', end='\n'):
    return sep.join([str(item) for item in items]) + end


if __name__ == '__main__':
    assert to_string(1, 2, 3) == '1 2 3\n'
    data = [7, 3, 1, "hello", (1, 2, 3)]
    assert to_string(*data, sep=", ", end="!") == '7, 3, 1, hello, (1, 2, 3)!'
