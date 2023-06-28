#  Спортивные гадания
#  Не знаю как решать.

from itertools import permutations, combinations, \
    combinations_with_replacement, product


def main(list_of_names):
    answer = []
    for i in combinations_with_replacement(sorted(list_of_names), 3):
        print(i)
    #     answer.append(', '.join(i))
    # return '\n'.join(answer)


if __name__ == '__main__':
    print(main([input() for _ in range(int(input()))]))
