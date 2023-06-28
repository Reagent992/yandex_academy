# Словарная ёлка
# Решение рабочее, но по заданию нужно использовать accumulate
local_tests = True


def main(list_of_words):
    """ a = ['мама', 'мыла', 'раму']"""
    answer = []
    for index, word in enumerate(list_of_words):
        answer.append(' '.join(list_of_words[0:index + 1]))
    return '\n'.join(answer)


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
