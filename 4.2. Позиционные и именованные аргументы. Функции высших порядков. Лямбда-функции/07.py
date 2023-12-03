"""
В эфире рубрика «Эксперименты»
https://new.contest.yandex.ru/41243/problem?id=149944/2022_11_06/Y5cuc2EWSP
Статус: Решено.
"""

data = list()


def enter_results(*args):
    """Добавление данных одного или нескольких результатов.
    количество параметров будет чётным"""
    args = list(args)
    [data.append(i) for i in zip(args[::2], args[1::2])]


def get_sum():
    """Возвращает пару сумм результатов экспериментов."""
    return (sum((i for i, _ in data)), sum((i for _, i in data)))


def get_average():
    """Возвращает пару средних арифметических
    значений результатов экспериментов."""
    i, g = get_sum()
    return round(i / len([i for i, _ in data]), 2), round(
        g / len([i for i, _ in data]), 2
    )


if __name__ == "__main__":
    enter_results(1, 2, 3, 4, 5, 6)
    print(get_sum(), get_average())
    enter_results(1, 2)
    print(get_sum(), get_average())
