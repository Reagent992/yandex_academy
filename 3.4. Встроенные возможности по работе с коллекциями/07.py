# Игровая сетка
# Верно.
from itertools import combinations


def main(list_of_words):
    answer = list(combinations(list_of_words, 2))
    for i in answer:
        print(i[0], '-', i[1])


if __name__ == '__main__':
    list_of_words = []
    for i in range(int(input())):
        list_of_words.append(input())
    main(list_of_words)
