# Меню питания 2.0
# Решать через itertools.islice
# Верно.
from itertools import islice, cycle


def main(porridge_list, kids):
    return '\n'.join(list(islice(cycle(porridge_list), kids)))


if __name__ == '__main__':
    amount_of_porridge = int(input())
    porridge_list = [input() for _ in range(amount_of_porridge)]
    kids = int(input())
    print(main(porridge_list, kids))
