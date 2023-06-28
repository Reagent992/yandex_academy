# Колода карт
# Верно.
from itertools import product


def main(word):
    suit = ['пик', 'треф', 'бубен', 'червей']
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама',
             'король', 'туз']
    suit.remove(word)
    for k, f in product(cards, suit):
        print(k, f)


if __name__ == '__main__':
    word = input()
    main(word)
