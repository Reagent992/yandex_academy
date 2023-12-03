"""
Генератор матриц
https://new.contest.yandex.ru/41243/problem?id=149944/2022_11_05/kQZsLlsTGU
Status: Solved.
"""


def make_matrix(size, value=0):
    if isinstance(size, int):
        return [[value for i in range(size)] for j in range(size)]
    else:
        return [[value for i in range(size[0])] for j in range(size[1])]


if __name__ == "__main__":
    assert make_matrix(3) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert make_matrix((4, 2), 1) == [[1, 1, 1, 1], [1, 1, 1, 1]]
