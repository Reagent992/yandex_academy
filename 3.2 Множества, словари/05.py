# неверно
def porridge(a, b, c):
    one_porridge_lover = set(c)

    if len(one_porridge_lover) != 0 and len(one_porridge_lover) != a \
            and len(one_porridge_lover) != b:
        print(len(one_porridge_lover))
    else:
        print('Таких нет')


if __name__ == '__main__':
    packages = [
        (3, 2, ['Васильев', 'Петров', 'Васечкин', 'Иванов', 'Михайлов']),
        (3, 3, ['Иванов', 'Петров', 'Васечкин', 'Иванов', 'Петров']),
        (3, 0, ['a', 'b', 'c']),  # баг
        (3, 3, ['a', 'b', 'c'])
    ]

    for a, b, c in packages:
        porridge(a, b, c)
