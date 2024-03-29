# Словарная ёлка
# Верно.
from itertools import accumulate

local_tests = False


def main(list_of_words):
    """ a = ['мама', 'мыла', 'раму']"""
    result = list(accumulate(
        list_of_words,
        lambda first, second: first + ' ' + second))
    return '\n'.join(result)


def tests():
    test_cases = {
        1: {
            'n': 'мама мыла раму',
            'answer': 'мама\nмама мыла\nмама мыла раму'
        }
    }
    for i in test_cases:
        func = main(test_cases[i]['n'].split())
        answer = test_cases[i]['answer']
        assert func == answer, f'Ошибка на тесте {i}, {func} != {answer}'
        print(f'############## Тест № {i}: OK ##################')


if __name__ == '__main__':
    if local_tests:
        tests()
    else:
        list_of_words = input().split()
        print(main(list_of_words))
