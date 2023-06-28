# Список покупок 2.0
# Результат: Верно.
from itertools import chain


def main(list_of_words):
    full_list = sorted(list(chain.from_iterable(list_of_words)))
    enum_list = [f'{index + 1}. {word.rstrip(",")}' for index, word in
                 enumerate(full_list)]
    return '\n'.join(enum_list)


if __name__ == '__main__':
    list_of_words = [input().split() for _ in range(int(input()))]
    print(main(list_of_words))
