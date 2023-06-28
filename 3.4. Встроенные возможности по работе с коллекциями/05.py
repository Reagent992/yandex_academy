# Список покупок
# Результат:
from itertools import chain

local_tests = False


def main(list_of_words):
    full_list = sorted(list(chain.from_iterable(list_of_words)))
    enum_list = [f'{index + 1}. {word.rstrip(",")}' for index, word in
                 enumerate(full_list)]
    return '\n'.join(enum_list)


def tests():
    test_cases = {
        1: {
            'n': [],
            'answer': ''
        }
    }
    for i in test_cases:
        func = main(test_cases[i])
        answer = test_cases[i]['answer']
        assert func == answer, f'Ошибка на тесте {i}, {func} != {answer}'
        print(f'_____________ Тест № {i}: OK _____________')


if __name__ == '__main__':
    if local_tests:
        tests()
    else:
        list_of_words = [input().split() for _ in range(3)]
        print(main(list_of_words))
