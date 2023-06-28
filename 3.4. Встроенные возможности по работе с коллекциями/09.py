# Таблица умножения 3.0
# Решать через itertools.product
# Верно.
from itertools import product


def main(number):
    f = range(1, number + 1)
    t = []
    for i in product(f, f):
        t.append(str(i[0] * i[1]))
        if i[1] == number:
            print(' '.join(t))
            t = []


if __name__ == '__main__':
    main(int(input()))
