# Расстановка спортсменов
# Верно.
from itertools import permutations


def main(list_of_names):
    answer = []
    for i in permutations(sorted(list_of_names)):
        answer.append(', '.join(i))
    return '\n'.join(answer)


if __name__ == '__main__':
    print(main([input() for _ in range(int(input()))]))
